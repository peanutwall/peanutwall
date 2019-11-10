import pandas as pd
import numpy as np
import os
from filterBean import *

pathHuman = r'c:/Users/31601/Desktop/checkData/test/commitmentSnake/results/human'
pathMax = r'c:/Users/31601/Desktop/checkData/test/commitmentSnake/results/maxModel'
pathSoftMax = r'c:/Users/31601/Desktop/checkData/test/commitmentSnake/results/softmax'

def get_file(path):  # 创建一个空列表
    files = os.listdir(path)
    files.sort()  # 排序
    list = []
    for file in files:
        if not os.path.isdir(path + file):  # 判断该文件是否是一个文件夹
            f_name = str(file)
            #             print(f_name)
            tr = '\\'  # 多增加一个斜杠
            filename = path + tr + f_name
            list.append(filename)
    return list

def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()

oldBeanRatioListHuman=[]
condition0IntentionOldListHuman=[]
ratioInNonCommitmentListHuman=[]
oldBeanRatioListMax=[]
condition0IntentionOldListMax=[]
ratioInNonCommitmentListMax=[]
oldBeanRatioListSoftMax=[]
condition0IntentionOldListSoftMax=[]
ratioInNonCommitmentListSoftMax=[]
list = get_file(pathHuman)
intentionOldHuman = []
intentionOldMax = []
intentionOldSoftMax = []
for i in range(len(list)):
    data = pd.read_csv(list[i])
    beanEaten = data["beanEaten"]
    condition = data["condition"]
    trajectory = data["trajectory"]
    goal = data["goal"]
    name = data['name']
    bean1GridX = data['bean1GridX']
    bean1GridY = data['bean1GridY']
    bean2GridX = data['bean2GridX']
    bean2GridY = data['bean2GridY']

    ratioInNonCommitment = calculateTrajectoryInNonCommitment(trajectory, bean1GridX, bean1GridY, bean2GridX, bean2GridY)
    ratioInNonCommitmentListHuman.append(ratioInNonCommitment)
    # oldBeanRatio = calculateOldBeanRatio(beanEaten)
    # oldBeanRatioListHuman.append(oldBeanRatio)
    #
    # condition0IntentionOld = calculateIntentionOld(condition, goal)
    # condition0IntentionOldListHuman.append(condition0IntentionOld)
    #
    # ratioInNonCommitment = calculateRatioInNonCommitment(goal)
    # ratioInNonCommitmentListHuman.append(ratioInNonCommitment)
    #
    # intentionOldHuman[0].append(calculateIntentionOldCondition(condition, intention, -5))
    # intentionOldHuman[1].append(calculateIntentionOldCondition(condition, intention, -3))
    # intentionOldHuman[2].append(calculateIntentionOldCondition(condition, intention, -1))
    # intentionOldHuman[3].append(calculateIntentionOldCondition(condition, intention, 0))
    # intentionOldHuman[4].append(calculateIntentionOldCondition(condition, intention, 1))
    # intentionOldHuman[5].append(calculateIntentionOldCondition(condition, intention, 3))
    # intentionOldHuman[6].append(calculateIntentionOldCondition(condition, intention, 5))


list = get_file(pathMax)
for i in range(len(list)):
    data = pd.read_csv(list[i])
    beanEaten = data["beanEaten"]
    condition = data["condition"]
    trajectory = data["trajectory"]
    goal = data["goal"]
    name = data['name']
    bean1GridX = data['bean1GridX']
    bean1GridY = data['bean1GridY']
    bean2GridX = data['bean2GridX']
    bean2GridY = data['bean2GridY']

    ratioInNonCommitment = calculateTrajectoryInNonCommitment(trajectory, bean1GridX, bean1GridY, bean2GridX, bean2GridY)
    ratioInNonCommitmentListMax.append(ratioInNonCommitment)

    # oldBeanRatio = calculateOldBeanRatio(beanEaten)
    # oldBeanRatioListMax.append(oldBeanRatio)
    #
    # condition0IntentionOld = calculateIntentionOld(condition, goal)
    # condition0IntentionOldListMax.append(condition0IntentionOld)
    #
    # ratioInNonCommitment = calculateRatioInNonCommitment(goal)
    # ratioInNonCommitmentListMax.append(ratioInNonCommitment)
    #
    # intentionOld[0].append(calculateIntentionOldCondition(condition, intention, -5))

list = get_file(pathSoftMax)
for i in range(len(list)):
    data = pd.read_csv(list[i])
    beanEaten = data["beanEaten"]
    condition = data["condition"]
    trajectory = data["trajectory"]
    goal = data["goal"]
    name = data['name']
    bean1GridX = data['bean1GridX']
    bean1GridY = data['bean1GridY']
    bean2GridX = data['bean2GridX']
    bean2GridY = data['bean2GridY']

    ratioInNonCommitment = calculateTrajectoryInNonCommitment(trajectory, bean1GridX, bean1GridY, bean2GridX, bean2GridY)
    ratioInNonCommitmentListSoftMax.append(ratioInNonCommitment)
    # oldBeanRatio = calculateOldBeanRatio(beanEaten)
    # oldBeanRatioListSoftMax.append(oldBeanRatio)
    #
    # condition0IntentionOld = calculateIntentionOld(condition, goal)
    # condition0IntentionOldListSoftMax.append(condition0IntentionOld)
    #
    # ratioInNonCommitment = calculateRatioInNonCommitment(goal)
    # ratioInNonCommitmentListSoftMax.append(ratioInNonCommitment)

# text_save('c:/Users/31601/Desktop/checkData/resultData/oldBeanRatioHuman.csv', oldBeanRatioListHuman)
# text_save('c:/Users/31601/Desktop/checkData/resultData/oldBeanRatioMax.csv', oldBeanRatioListMax)
# text_save('c:/Users/31601/Desktop/checkData/resultData/oldBeanRatioSoftMax.csv', oldBeanRatioListSoftMax)
# text_save('c:/Users/31601/Desktop/checkData/resultData/condition0IntentionOldHuman.csv', condition0IntentionOldListHuman)
# text_save('c:/Users/31601/Desktop/checkData/resultData/condition0IntentionOldMax.csv', condition0IntentionOldListMax)
# text_save('c:/Users/31601/Desktop/checkData/resultData/condition0IntentionOldSoftMax.csv', condition0IntentionOldListSoftMax)
# text_save('c:/Users/31601/Desktop/checkData/resultData/ratioInNonCommitmentHuman.csv', ratioInNonCommitmentListHuman)
# text_save('c:/Users/31601/Desktop/checkData/resultData/ratioInNonCommitmentMax.csv', ratioInNonCommitmentListMax)
# text_save('c:/Users/31601/Desktop/checkData/resultData/ratioInNonCommitmentSoftMax.csv', ratioInNonCommitmentListSoftMax)

print(np.mean(ratioInNonCommitmentListHuman))
print(np.std(ratioInNonCommitmentListHuman))
print(np.mean(ratioInNonCommitmentListMax))
print(np.std(ratioInNonCommitmentListMax))
print(np.mean(ratioInNonCommitmentListSoftMax))
print(np.std(ratioInNonCommitmentListSoftMax))