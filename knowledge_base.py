from Rule import Rule
from Fact import Fact
import forward_chain

class knowledge_base:
    def __init__(self, strings):
        self.facts = set()
        self.rules = []

        for string in strings:
            string = string[0:-1]
            if (string.startswith('/*') and string.endswith('*/')) or string.startswith('/*'):
                continue

            elif ':-' in string:
                rule = Rule.parse_rule(string)
                self.addRule(rule)

            elif not ':-' in string and '(' in string:
                fact = Fact.parse_fact(string)
                self.addFact(fact)

    def addFact(self, fact):
        self.facts.add(fact)

    def addRule(self, rule):
        self.rules.append(rule)

    def querry(self, q):
        return forward_chain.ForwardChain(self, q)

    def addFacts(self, facts):
        for fact in facts:
            self.facts.add(fact)
