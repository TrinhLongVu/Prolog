import itertools
from Fact import Fact

def unify(x, y, theta):
    def getType(x):
        if type(x) is str:
            if len(x) > 0:
                if x[0].isupper():
                    return 'var'
        elif type(x) is Fact:
            return 'fact'
        elif type(x) is list:
            return 'list'

    if theta == False:  # Nếu theta False tức là không có phép thế phù hợp, trả về False
        return False
    if x == y:  # Nếu x==y tức là đã đồng nhất thành công, trả về phép thế theta
        return theta
    if getType(x) == 'var':  # Nếu x là biến
        if x in theta:
            # thì đi đồng nhất x,y với x=something thuộc theta
            return unify(theta[x], y, theta)
        if y in theta:  # Nếu y có trong theta
            # thì đi đồng nhất x,y với y=something thuộc theta
            return unify(x, theta[y], theta)
        theta[x] = y  # Nếu không tìm được phép thế theta=something, tạo phép thế x=y
        return theta
    if getType(y) == 'var':  # Nếu y là biến
        return unify(y, x, theta)  # Gọi hàm làm tương tự như x
    # Nếu x là một tri thức,và y cũng là một tri thức
    if getType(x) == 'fact' and getType(y) == 'fact':
        # Đi đồng nhất mối quan hệ và danh sách tham số của tri thức đó
        return unify(x.args, y.args, unify(x.oper, y.oper, theta))
    # Nếu x và y là một danh sách các tham số của tri thức
    if getType(x) == 'list' and getType(y) == 'list':
        # Đi đồng nhất từng cặp tham số
        return unify(x[1:], y[1:], unify(x[0], y[0], theta))
    return False

def ForwardChain(kb, querry):
    def CheckTheta(theta, rule):
        if not theta:
            return False
        for condition in rule.conditions:
            if condition[2] == 0:
                if theta[condition[0]] != theta[condition[1]]:
                    return False
            elif condition[2] == 1:
                if theta[condition[0]] == theta[condition[1]]:
                    return False
        return True

    def SubsFacts(fact1, fact2):
        if len(fact1) != len(fact2):
            return False
        for f1, f2 in zip(fact1, fact2):
            if f1.oper != f2.oper:
                return False
        theta = {}
        return unify(fact1, fact2, theta)

    def GetPotentialFacts(rule, kb):
        result = set()
        for fact in kb:
            if fact.oper in rule.opers:
                result.add(fact)
        result = list(result)
        result.sort()
        return result

    def CheckTriggered(rule, facts):
        for newFact in facts:
            for premise in rule.premises:
                if unify(newFact, premise, {}):
                    return True
        return False

    result = set()
    theta = {}
    for fact in kb.facts:
        # Kiểm tra xem truy vấn đã có sẵn trong KB chưa
        theta = unify(fact, querry, {})
        if theta != False:
            if len(theta) == 0:  # Nếu theta rỗng, truy vấn có thể được thỏa mãn bằng mọi phép thế
                result.add('true')
                return result
            result.add(str(theta))  # Nếu tồn tại theta, thêm theta vào kết quả

    prevFacts = kb.facts.copy()  # Mang ý nghĩa tri thức vừa được sinh ra
    # Ban đầu là toàn bộ tri thức ban đầu
    while True:
        new = set()
        for rule in kb.rules:  # Với mỗi rule thuộc KB
            # Kiểm tra xem rule này có thể được kích hoạt
            if not CheckTriggered(rule, prevFacts):
                continue  # Từ các fact mới sinh ra không
                # Nếu không, tức là Rule này không thể được kích hoạt từ toàn bộ KB, đến với rule tiếp theo
                # Vì các fact trước đó cũng đã được kiểm tra xem có kích hoạt được rule hay không
                # Nếu có, thu thập tất cả các fact có thể kích hoạt được rule trong KB
            # bằng hàm GetPotentialFacts(rule,kb.facts)
            potential_fact = GetPotentialFacts(rule, kb.facts)

            count = len(rule.premises)
            # Nếu các premise(tiền đề) của rule có 2 fact giống nhau
            if rule.dup_pred:
                potential_premises = itertools.permutations(
                    potential_fact, count)  # Ta sinh chỉnh hợp

            else:
                potential_premises = itertools.combinations(
                    potential_fact, count)  # Ta sinh tổ hợp
            # Việc sinh chỉnh hợp tổ hợp các fact nhằm mục đích match các fact có sẵn với các premise của rule
            # Vì các fact trong potential_premises đã được sort nên việc lấy tổ hợp cũng đã ngầm lấy các fact có thứ tự

            for tuple_premises in potential_premises:  # Với mỗi bộ fact sinh được
                premises = list(tuple_premises)
                # Kiểm tra xem có thể đồng nhất được tule không
                theta = SubsFacts(rule.premises, premises)
                # Sau đó gọi hàm kiểm tra xem phép thế theta
                if not CheckTheta(theta, rule):
                    # có thỏa mãn điểu kiện của tule hay không
                    continue
                q = rule.result.copy()  # Nếu theta hợp lệ, nghĩa là result của rule được kích hoạt
                for i in range(len(q.args)):  # Đồng nhất các tham số của q với phép thế theta
                    if q.args[i] in theta:
                        q.args[i] = theta[q.args[i]]

                if q not in prevFacts and q not in kb.facts:  # Nếu q chưa từng được sinh ra
                    new.add(q)  # Thêm q vào bộ các fact mới được sinh
                    # Kiểm tra xem q có thỏa mãn truy vấn không
                    phi = unify(q, querry, {})
                    if phi:  # Nếu có
                        if len(phi) == 0:  # Truy vấn có thể thỏa mãn bằng mọi phép thế
                            kb.addFacts(new)
                            result.add('true')
                            return result
                        # Truy vấn có thể thỏa mãn bằng phép thế phi
                        result.add(str(phi))

        if not new:  # Nếu không có tri thức nào mới được sinh ra, dừng
            if not result:
                result.add('false')
            return result
        prevFacts = new
        kb.addFacts(new)
