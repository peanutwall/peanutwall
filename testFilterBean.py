import os
import sys

DIRNAME = os.path.dirname(__file__)
sys.path.append(os.path.join(DIRNAME))
import unittest
from ddt import ddt, data, unpack
import numpy as np
from filterBean import *

@ddt
class TestFilterFunctions(unittest.TestCase):
    def setUp(self):
        self.testParameter = 0
    @data(((1,2,1,2),0.5),\
          ((1,1,1,1,1),1),\
          ((2,2,2),0))
    @unpack
    def testCalculateOldBeanRatio(self,beanEaten, groundTruthRatio):
        oldBeanRatio = calculateOldBeanRatio(beanEaten)
        truthValue = np.array_equal(oldBeanRatio, groundTruthRatio)
        self.assertTrue(truthValue)

    @data((('1','3','5','0','0'),(['2','0'],['1','0'],['1','1'],['1','0'],['2','0']),0.5),\
          (('0','0','0'),(['0','0','1'],['0','0','1'],['0','0','1']),1),\
          (('0','1','0'),(['2','2'],['2','1','2'],['2','2','2','0','0']),0))
    @unpack
    def testCalculateIntentionOld(self,vector1,vector2, groundTruthIntention):
        condition0IntentionOld = calculateIntentionOld(vector1, vector2)
        truthValue = np.array_equal(condition0IntentionOld, groundTruthIntention)
        self.assertTrue(truthValue)

    @data(([['0', '2', '0', '2']],0.25),\
          ([['2', '0']],0),\
          ([['0', '0']],1))
    @unpack
    def testCalculateRatioInNonCommitment(self, vector1, groundTruthRatioInNonCommitment):
        ratioInNonCommitment = calculateRatioInNonCommitment(vector1)
        truthValue = np.array_equal(ratioInNonCommitment, groundTruthRatioInNonCommitment)
        self.assertTrue(truthValue)

    @data((('-1','3','5','0','0'),(['1','0'],['1','0'],['1','1'],['1','0'],['2','0']), -1, 1),\
          (('0','3','3'),(['0','0','1'],['0','2','1'],['0','0','1']), 3, 0.5),\
          (('5','1','0'),(['2','2'],['2','1','2'],['2','2','2','0','0']), 5, 0))
    @unpack
    def testCalculateIntentionOldCondition(self, condition, goal, distance, groundTruthIntentionOldCondition):
        IntentionOldCondition = calculateIntentionOldCondition(condition, goal, distance)
        truthValue = np.array_equal(IntentionOldCondition, groundTruthIntentionOldCondition)
        self.assertTrue(truthValue)


    @data((['[1,1], [1,2], [1,3], [1,4], [1,5]'], ['1'], ['5'], ['5'], ['3'], 0.4),\
          (['[1,1], [1,2], [1,3], [1,2], [2,2], [2,3]'], ['2'], ['3'], ['5'], ['2'], 1/6),\
          (['[1,1], [2,1], [1,1], [2,1], [2,2]'], ['2'], ['2'], ['5'], ['1'], 0.6))
    @unpack
    def testCalculateTrajectoryInNonCommitment(self, trajectory, bean1GridX, bean1GridY, bean2GridX, bean2GridY, groundTruth):
        trajectoryInNonCommitment = calculateTrajectoryInNonCommitment(trajectory, bean1GridX, bean1GridY, bean2GridX, bean2GridY)
        truthValue = np.array_equal(trajectoryInNonCommitment, groundTruth)
        self.assertTrue(truthValue)


if __name__ == '__main__':
    unittest.main()

print(calculateTrajectoryInNonCommitment(['[1,1], [1,2], [1,3], [1,2], [2,2], [2,3]'], ['2'], ['3'], ['5'], ['2']))
