from contextlib import nullcontext



class ResultCoin(object):

    resultCoin = {}
    # 싱글톤 
    def __new__(cls):
        if not hasattr(cls,'instance'):
                print('create')
                cls.instance = super(ResultCoin, cls).__new__(cls)
        else:
                print('recycle')
        return cls.instance

    def getResultCoin(self,coinName):
        
        resultValue = -1

        if(self.resultCoin[coinName] != None):
            print(self.resultCoin[coinName])
            resultValue = self.resultCoin[coinName]
    
        return resultValue

    def setResultCoin(self,coinName,buyPrice):
        self.resultCoin[coinName] = buyPrice

