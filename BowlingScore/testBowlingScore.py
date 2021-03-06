 
from bowlingScoreClass import *
import unittest


class TestBowlingScore(unittest.TestCase):

    def test_BowlingScore(self):
        scores = bowlingScore()
        framesScoreList = 'X X X X X X X X X X X X'
        totalScore = scores.getTotalScore(framesScoreList)
        self.assertEqual(totalScore, 300, "Correct")
        
        scores = bowlingScore()
        framesScoreList = '9- 9- 9- 9- 9- 9- 9- 9- 9- 9-'
        totalScore = scores.getTotalScore(framesScoreList)
        self.assertEqual(totalScore, 90, "Correct")
        
        scores = bowlingScore()
        framesScoreList = '5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5'
        totalScore = scores.getTotalScore(framesScoreList)
        self.assertEqual(totalScore, 150, "Correct")
        
        scores = bowlingScore()
        framesScoreList = '6/ 6/ 6/ 6/ 6/ 6/ 6/ 6/ 6/ 6/6'
        totalScore = scores.getTotalScore(framesScoreList)
        self.assertEqual(totalScore, 160, "Correct")
        
        scores = bowlingScore()
        framesScoreList = '6/ 6/ 6/ 6/ 6/ 6/ 6/ 6/ 6/ 6/4'
        totalScore = scores.getTotalScore(framesScoreList)
        self.assertEqual(totalScore, 158, "Correct")
        
        
        
if __name__ == '__main__':
    unittest.main()
