class Fact:
    def __init__(self, oper, args, neg=False):
        self.oper = oper
        self.args = args
        self.neg = neg

    def __repr__(self):
        return '{}({})'.format(self.oper, ', '.join(self.args))

    def __lt__(self, rhs):
        if self.oper != rhs.oper:
            return self.oper < rhs.oper
        if self.neg != rhs.neg:
            return self.neg < rhs.neg
        return self.args < rhs.args

    def __eq__(self, rhs):
        if self.oper != rhs.oper:
            return False
        if self.neg != rhs.neg:
            return False
        return self.args == rhs.args

    def __hash__(self):
        return hash(str(self))

    @staticmethod
    def ParseFact(fact):
        fact = fact.strip().rstrip('.').replace(' ', '')
        sepIdx = fact.index('(')
        op = fact[:sepIdx]
        args = fact[sepIdx + 1 : -1].split(',')
        return Fact(op, args)

    def Copy(self):
        return Fact(self.oper, self.args.copy(), self.neg)
