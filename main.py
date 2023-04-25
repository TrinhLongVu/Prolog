from knowledge_base import KnowledgeBase
import forward_chain
from rule import Fact

def Run():
    def ReadFile(fileName):
        f = open(fileName, 'r')
        return f.readlines()

    def GetType(sentStr):
        sentStr = sentStr.strip()
        if not sentStr:
            return 'blank'
        if sentStr.startswith('/*') and sentStr.endswith('*/'):
            return 'comment'
        if ':-' in sentStr:
            return 'rule'
        return 'fact'

    knowledgesData = ReadFile("test/knowledge.pl")
    output = open('test/output.txt', 'w')
    querryDatas = ReadFile("test/query.pl")

    querry = set()
    kb = KnowledgeBase(knowledgesData)

    for querryData in querryDatas:
        querryData = querryData[0:-1]
        type = GetType(querryData)
        if type == 'fact':
            fact = Fact.ParseFact(querryData)
            querry.add(fact)

    querry = list(querry)

    for que in querry:
        answer=forward_chain.ForwardChain(kb,que)
        print(que)
        print(answer)

        output.write(str(que))
        output.write('\n')
        output.write(str(answer))
        output.write('\n')
        output.write('\n')


if __name__ == "__main__":
    Run()
