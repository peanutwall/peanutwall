oldBeanRatio: 吃旧的豆子的概率
condition0IntentionOld: 在两个豆子距离一样的条件下吃就豆子的概率
ratioInNonCommitment: 轨迹在避免承诺区的概率

filterBean.py 里包含了几个主要函数
testfilterBean.py里包含了unittest


checkData.py是处理数据的代码，根据human，max，softmax三个文件夹里的数据，将结果存储在resultData中
如：
oldBeanRatioListHuman就是储存human文件夹里所有被试吃旧豆子的概率的列表
数据结果的平均值和标准差储存在resultData.xlsx里面

后续又做了distance不同时firstIntention和oldBeanEaten的测试，结果储存在resultDataDistance和resultOfBeanEaten里

因为原始数据集太大了，如果要运行数据处理代码checkData的话请把那个test文件夹加入到这个文件夹里，然后修改一下路径名

