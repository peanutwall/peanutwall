import pandas as pd
import numpy as np


# data = pd.read_csv('c:/Users/31601/Desktop/checkData/human.csv')
# beanEaten = data["beanEaten"]
# condition = data["condition"]
# trajectory = data["trajectory"]
# goal = data["goal"]
# name = data['name']
#旧豆子比例

def calculateOldBeanRatio(beanEaten):
    oldBean = 0
    for i in range(len(beanEaten)):
        if beanEaten[i] == 1:
            oldBean = oldBean + 1
    oldBeanRatio = oldBean / len(beanEaten)
    return oldBeanRatio




#distance = 0, intention为旧豆子的比例

def calculateIntentionOld(condition, goal):
    intentionOld = 0
    condition0 = 0
    for i in range(len(condition)):
        if condition[i] == '0':
            condition0 = condition0 + 1
            for j in range(len(goal[i])):
                if goal[i][j] == '1':
                    intentionOld = intentionOld + 1
                    break
    condition0IntentionOld = intentionOld / condition0
    return condition0IntentionOld

def calculateIntentionOld(condition, goal):
    intentionOld = 0
    condition0 = 0
    for i in range(len(condition)):
        if condition[i] == '0':
            condition0 = condition0 + 1
            for j in range(len(goal[i])):
                if goal[i][j] == '2':
                    break
                if goal[i][j] == '1':
                    intentionOld = intentionOld + 1
                    break
    condition0IntentionOld = intentionOld / condition0
    return condition0IntentionOld

# def calculateIntentionOld(condition, goal):
#     intentionOld = 0
#     condition0 = 0
#     for i in range(len(condition)):
#         if condition[i] == '0':
#             condition0 = condition0 + 1
#             for j in range(len(goal[i])):
#                 if goal[i][j] == '2':
#                     break
#                 if goal[i][j] == '1':
#                     intentionOld = intentionOld + 1
#                     break
#     condition0IntentionOld = intentionOld / condition0
#     return condition0IntentionOld

def calculateIntentionOldCondition(condition, goal, distance):
    intentionOld = 0
    conditionDistance = 0
    for i in range(len(condition)):
        if condition[i] == str(distance):
            conditionDistance = conditionDistance + 1
            for j in range(len(goal[i])):
                if goal[i][j] == '2':
                    break
                if goal[i][j] == '1':
                    intentionOld = intentionOld + 1
                    break
    intentionOldCondition = intentionOld / conditionDistance
    return intentionOldCondition

def calculateBeanEatenOldCondition(condition, beanEaten, distance):
    beanEatenOld = 0
    conditionDistance = 0
    for i in range(len(condition)):
        if condition[i] == str(distance):
            conditionDistance = conditionDistance + 1
            if beanEaten[i] == 1:
                beanEatenOld = intentionOld + 1
    beanEatenOldRatio = beanEatenOld / conditionDistance
    return beanEatenOldRatio


def calculateRatioInNonCommitment(goal):
    trajectoryInNonCommitment = 0
    trajectoryLength = 0
    ratioInNonCommitmentList = []
    for i in range(len(goal)):
        flag = 0
        trajectoryInNonCommitment = 0
        trajectoryLength = 0
        for j in range(len(goal[i])):
            if goal[i][j] == '1' or goal[i][j] == '2':
                flag = 1
            if flag == 0:
                if goal[i][j] == '0':
                    trajectoryInNonCommitment = trajectoryInNonCommitment + 1
            if goal[i][j] == '1' or goal[i][j] == '2' or goal[i][j] == '0':
                trajectoryLength = trajectoryLength + 1
        ratioInNonCommitmentList.append(trajectoryInNonCommitment / trajectoryLength)
    ratioInNonCommitment = np.mean(ratioInNonCommitmentList)
    return ratioInNonCommitment
#轨迹在避免承诺区的比例(使用goal中intention之前0的数量）
def generateTempTrajectory(trajectory):
    tempTrajectory = []
    for j in range(len(trajectory)):
        if trajectory[j].isdigit() and trajectory[min(j + 1, len(trajectory)-1)].isdigit():
            tempTrajectory.append(int(trajectory[j]) * 10 + int(trajectory[j + 1]))
        elif trajectory[j].isdigit() and not trajectory[max(j - 1, 0)].isdigit():
            tempTrajectory.append(int(trajectory[j]))
    return tempTrajectory

# print(trajectory[4])
# print(generateTempTrajectory(trajectory[4]))
# print(len(generateTempTrajectory(trajectory[4])))


def calculateTrajectoryInNonCommitment(trajectory, bean1GridX, bean1GridY, bean2GridX, bean2GridY):
    ratioInNonCommitmentList = []
    for i in range(len(trajectory)):
        trajectoryInNonCommitment = 0
        tempTrajectory = generateTempTrajectory(trajectory[i])
        if int(bean1GridX[i]) > int(tempTrajectory[0]) and int(bean2GridX[i]) > int(tempTrajectory[0]):
            xLimit = min(int(bean1GridX[i]), int(bean2GridX[i]))
        elif int(bean1GridX[i]) < int(tempTrajectory[0]) and int(bean2GridX[i]) < int(tempTrajectory[0]):
            xLimit = max(int(bean1GridX[i]), int(bean2GridX[i]))
        else:
            xLimit = tempTrajectory[0]

        if int(bean1GridY[i]) > int(tempTrajectory[1]) and int(bean2GridY[i]) > int(tempTrajectory[1]):
            yLimit = min(int(bean1GridY[i]), int(bean2GridY[i]))
        elif int(bean1GridY[i]) < int(tempTrajectory[1]) and int(bean2GridY[i]) < int(tempTrajectory[1]):
            yLimit = max(int(bean1GridY[i]), int(bean2GridY[i]))
        else:
            yLimit = tempTrajectory[1]
        for j in range(int(len(tempTrajectory)/2)):
            if min(xLimit, tempTrajectory[0]) <= tempTrajectory[j*2] <= max(xLimit, tempTrajectory[0]) and min(yLimit, tempTrajectory[1]) <= tempTrajectory[j*2+1] <= max(yLimit, tempTrajectory[1]):
                trajectoryInNonCommitment = trajectoryInNonCommitment + 1
            else:
                break
        ratioInNonCommitment = (trajectoryInNonCommitment-1) / (len(tempTrajectory) / 2)
        ratioInNonCommitmentList.append(ratioInNonCommitment)
    return np.mean(ratioInNonCommitmentList)



