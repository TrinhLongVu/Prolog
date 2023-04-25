from rule import Rule
from fact import Fact
import forward_chain

class KnowledgeBase:
    def __init__(self, strings):
        self.facts = set()
        self.rules = []

        for string in strings:
            string = string[0:-1]
            if (string.startswith('/*') and string.endswith('*/')) or string.startswith('/*'):
                continue

            elif ':-' in string:
                rule = Rule.ParseRule(string)
                self.AddRule(rule)

            elif not ':-' in string and '(' in string:
                fact = Fact.ParseFact(string)
                self.AddFact(fact)

    def AddFact(self, fact):
        self.facts.add(fact)

    def AddRule(self, rule):
        self.rules.append(rule)

    def Querry(self, q):
        return forward_chain.ForwardChain(self, q)

    def AddFacts(self, facts):
        for fact in facts:
            self.facts.add(fact)
