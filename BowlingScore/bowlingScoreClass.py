NUMFRAMES = 10
NUMPINS = 10

class bowlingScore():
    
    def __init__(self):
        pass
            
    def getTotalScore(self,scoreString):
        self.__getScoreString(scoreString)
        self.__calcSingleFrameValueList(self.scoreString)
        return sum(self.scoreListValues)
   
    # Private methods
    def __getScoreString(self,scoreString):
        self.scoreString = scoreString
        
    def __getScoreList(self,scoreString):
        return scoreString.split(' ')
            
    def __interpSingleFrameValue(self, scoreSymbol):
        if scoreSymbol == 'X':
            scoreValue = ['strike',10,0]
        
        elif scoreSymbol.find('-')>0:
            scoreValue = ['',int(scoreSymbol[0]),0]
        
        elif scoreSymbol.find('/')>0:
            if len(scoreSymbol) == 2:
                scoreValue = ['spare',int(scoreSymbol[0]),NUMPINS-int(scoreSymbol[0])]
            else:
                scoreValue = ['spare',int(scoreSymbol[0]),NUMPINS-int(scoreSymbol[0]),int(scoreSymbol[2])]
        
        else:
            raise Exception('score symbol undefined!')
        
        return scoreValue
        
    def __calcSingleFrameValueList(self,scoreString):
        scoreList = self.__getScoreList(scoreString)
        lenScoreList = len(scoreList)
        scoreListValues = []
        for idx in range(NUMFRAMES):
            val = []
            val_1stNext = []
            val_2ndNext = []
            
            val = self.__interpSingleFrameValue(scoreList[idx])
            if val[0] == 'strike':
                val_1stNext = self.__interpSingleFrameValue(scoreList[idx+1])
                if val_1stNext[0] == 'strike':
                    val_2ndNext = self.__interpSingleFrameValue(scoreList[idx+1])
                    scoreListValues.append(val[1]+val_1stNext[1]+val_2ndNext[1])
                else:
                    scoreListValues.append(val[1]+val_1stNext[1]+val_1stNext[2])
            
            elif val[0] == 'spare':
                if (idx+1)<lenScoreList:
                    val_1stNext = self.__interpSingleFrameValue(scoreList[idx+1])
                    scoreListValues.append(NUMPINS+val_1stNext[1])
                else:
                    scoreListValues.append(sum(val[1:]))
            
            else:
                scoreListValues.append(val[1])
        self.scoreListValues = scoreListValues
        
            
    
                    
   