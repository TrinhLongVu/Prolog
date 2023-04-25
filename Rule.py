from fact import Fact

class Rule:
    def __init__(self, result, premises, conditions=[]):
        self.result = result
        self.premises = premises
        self.conditions = conditions

        self.opers = set()
        for premise in self.premises:
            self.opers.add(premise.oper)

        self.premises.sort()
        self.dupPred = False
        for i in range(len(self.premises)-1):
            if self.premises[i].oper == self.premises[i+1].oper:
                self.dupPred = True
                break

    def __repr__(self):
        return '{} => {}, conditions:{}.'.format(' & '.join([str(cond) for cond in self.premises]), str(self.result), str(self.conditions))

    def ProcessCondition(string):
        if ',' in string:
            conditions = string.split(',')
        else:
            conditions = [string]
        result = []

        for i in range(len(conditions)):
            if '\=' in conditions[i]:
                phrase = conditions[i].split('\=')
                phrase.extend([1])
                result.append(phrase)
            else:
                phrase = conditions[i].split('=')
                phrase.extend([0])
                result.append(phrase)
        return result

    @staticmethod
    def ParseRule(rule):
        rule = rule.replace(' ', '')
        rule = rule.replace('.', '')
        sepId = rule.find(':-')
        concludsion = Fact.ParseFact(rule[:sepId])
        premises = []
        conditions = []
        listPremises = rule[sepId+2:].split('),')

        if '=' in listPremises[-1]:
            conditions = Rule.ProcessCondition(listPremises[-1])
            listPremises = listPremises[:-1]

            for i in range(len(listPremises)):
                listPremises[i] = listPremises[i] + ')'
        else:
            for i in range(len(listPremises[:-1])):
                listPremises[i] = listPremises[i] + ')'

        for premise in listPremises:
            premises.append(Fact.ParseFact(premise))

        return Rule(concludsion, premises, conditions)
