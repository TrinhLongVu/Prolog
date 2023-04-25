import itertools
from fact import Fact

def Unify(x, y, theta):
    def GetType(x):
        if type(x) is str:
            if len(x) > 0:
                if x[0].isupper():
                    return 'var'
        elif type(x) is Fact:
            return 'fact'
        elif type(x) is list:
            return 'list'

    if theta == False:  # If theta False i.e. there is no matching substitution, return False
        return False
    if x == y:  # If x==y is successfully matched, the theta . substitution is returned
        return theta
    if GetType(x) == 'var':  # If x is a variable
        if x in theta:  # If x is in theta
            return Unify(theta[x], y, theta)  # identify x,y with x=something of theta
        if y in theta:  # If y is in theta
            return Unify(x, theta[y], theta)  # identify x,y with y=something of theta
        theta[x] = y  # If the theta=something cannot be found, make the substitution x=y
        return theta
    if GetType(y) == 'var':  # If y is a variable
        return Unify(y, x, theta)  # do the same as x
    
    if GetType(x) == 'fact' and GetType(y) == 'fact':  # If x is a fact, and y is also a fact
        return Unify(x.args, y.args, Unify(x.oper, y.oper, theta))  # Identify the relationship and parameter list of that knowledge
    if GetType(x) == 'list' and GetType(y) == 'list':  #if x and y are a 'list'
        return Unify(x[1:], y[1:], Unify(x[0], y[0], theta))  # Homogenize each pair of parameters
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
        return Unify(fact1, fact2, theta)

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
                if Unify(newFact, premise, {}):
                    return True
        return False

    result = set()
    theta = {}
    for fact in kb.facts:
        # Check if the query is already in the KB
        theta = Unify(fact, querry, {})
        if theta != False:
            if len(theta) == 0:  # If theta is empty, the query can be satisfied by any substitution
                result.add('true')
                return result
            result.add(str(theta))  # If theta exists, add theta to the result

    prevFacts = kb.facts.copy()
    while True:
        new = set()
        for rule in kb.rules:
            # check if each KB rule can be activated from the newly generated facts
            if not CheckTriggered(rule, prevFacts):
                continue  
                # Otherwise, this rule cannot be activated from the entire KB, go to the next rule
                # Because the previous facts have also been checked to see if the rule can be activated
                # If yes, collect all the facts that can trigger the rule in the KB using the function GetPotentialFacts(rule,kb.facts)
            potentialFact = GetPotentialFacts(rule, kb.facts)

            count = len(rule.premises)
            # Check if rule contains premises with the same predicate
            if rule.dupPred:
                potentialPremises = itertools.permutations(potentialFact, count)  # arrangement
            else:
                potentialPremises = itertools.combinations(potentialFact, count)  # combination
            # The biosynthesis and combination of facts Intent in accordance with the available facts with the premise of the rule
              # Since events in potentialPremises are sorted, combing has also stopped fetching ordered events

            for tuplePremises in potentialPremises:  
                premises = list(tuplePremises)

                theta = SubsFacts(rule.premises, premises)
                if not CheckTheta(theta, rule):
                    continue
                q = rule.result.Copy()  
                for i in range(len(q.args)):  
                    if q.args[i] in theta:
                        q.args[i] = theta[q.args[i]]

                if q not in prevFacts and q not in kb.facts:  
                    new.add(q)  
                    phi = Unify(q, querry, {})
                    if phi:  
                        if len(phi) == 0:  
                            kb.AddFacts(new)
                            result.add('true')
                            return result
                        result.add(str(phi))

        if not new:  
            if not result:
                result.add('false')
            return result
        prevFacts = new
        kb.AddFacts(new)
