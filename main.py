from knowledge_base import knowledge_base
import forward_chain
from Rule import Fact

def run():
    def ReadFile(file_name):
        f = open(file_name, 'r')
        return f.readlines()

    def getType(sent_str):
        sent_str = sent_str.strip()
        if not sent_str:
            return 'blank'
        if sent_str.startswith('/*') and sent_str.endswith('*/'):
            return 'comment'
        if ':-' in sent_str:
            return 'rule'
        return 'fact'

    knowledgesData = ReadFile("test/knowledge.pl")
    output = open('test/output.txt', 'w')
    querryDatas = ReadFile("test/query.pl")

    querry = set()
    kb = knowledge_base(knowledgesData)

    for querryData in querryDatas:
        querryData = querryData[0:-1]
        type = getType(querryData)
        if type == 'fact':
            fact = Fact.parse_fact(querryData)
            querry.add(fact)

    querry = list(querry)

    for i in range(len(querry)):
        theta = forward_chain.ForwardChain(kb, querry[i])
        output.write(str(querry[i]))
        output.write('\n')
        output.write(str(theta))
        output.write('\n')
        output.write('\n')

if __name__ == "__main__":
    run()
