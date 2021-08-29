# coding=utf-8
"""
tfidf 特征文本聚类（tfidf特征提取会很消耗内存。因此文本太大无法使用该方法）
三种聚类算法：Kmeans DBSCAN GMM（其中GMM很慢）
输入：prepro.py 形成的pkl文件
输出：聚类图形
      每一类的每条微博内容 ："cluster1.txt" 、"cluster2.txt" 、"cluster3.txt" 、"cluster4.txt"
参数：weight权重 这是一个重要参数
"""

import time
import re
import os
import sys
import codecs
import pickle
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.mixture import GaussianMixture

from matplotlib.font_manager import *

from sklearn.decomposition import PCA
import shutil
import numpy as np
import matplotlib
import scipy
import matplotlib.pyplot as plt
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer

if __name__ == "__main__":

    #########################################################################
    #                           step 1 calculate TFIDF

    # Document expected and space link

    corpus = []
    content_comment = pickle.load(open('Agu.pkl', 'rb'))


    # 读取预料 一行预料为一个文档
    # Read the expected and one line is expected to be a document
    for i in content_comment:
        corpus.append(' '.join(i[1]))
    # print(corpus)

    # 参考: http://blog.csdn.net/abcjennifer/article/details/23615947
    # vectorizer = HashingVectorizer(n_features = 4000)

    # 将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
    # Convert the words in the text into a word frequency matrix. 
    # The matrix element a[i][j] represents the word frequency of word j in type i text
    vectorizer = CountVectorizer()

    # 该类会统计每个词语的tf-idf权值
    #This class will count the tf-idf weight of each word
    transformer = TfidfTransformer()

    # 第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵
    # The first fit_transform is to calculate tf-idf.
    # the second fit_transform is to convert the text into a word frequency matrix
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))

    # 获取词袋模型中的所有词语
    # Get all words in the bag of words model
    word = vectorizer.get_feature_names()
    print("word...")
    print(word)

    # 将tf-idf矩阵抽取出来，元素w[i][j]表示j词在i类文本中的tf-idf权重
    # Extract the tf-idf matrix.
    # the element w[i][j] represents the tf-idf weight of word j in type i text
    weight = tfidf.toarray()
    print("weight...")    # list of list格式
    # print(weight[200:])


    # 打印特征向量文本内容
    # Print feature vector text content
    print('Features length: ' + str(len(word)))
    
    # 写特征文件太大了
    '''
    resName = "BHTfidf_Result.txt"
    result = codecs.open(resName, 'w', 'utf-8')
    for j in range(len(word)):
        result.write(word[j] + ' ')
    result.write('\r\n\r\n')

    # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
    for i in range(len(weight)):
        # print u"-------这里输出第", i, u"类文本的词语tf-idf权重------"
        for j in range(len(word)):
            # print weight[i][j],
            result.write(str(weight[i][j]) + ' ')
        result.write('\r\n\r\n')

    result.close()
    '''
    ########################################################################
    #                             Step2 Kmeans Cluster

    print('Start Kmeans:')

    clf = KMeans(n_clusters=3)  # Scenic animal characters country
    s = clf.fit(weight)
    print(s)

    
    # print 'Start MiniBatchKmeans:'
    # from sklearn.cluster import MiniBatchKMeans
    # clf = MiniBatchKMeans(n_clusters=20)
    # s = clf.fit(weight)
    # print s
    
    
    # 中心点
    # print(clf.cluster_centers_)

    # 每个样本所属的簇
    # The cluster to which each sample belongs
    label = []  # Store 1000 class labels 4 classes
    print(clf.labels_)
    i = 1
    while i <= len(clf.labels_):
        print(i, clf.labels_[i - 1])
        label.append(clf.labels_[i - 1])
        i = i + 1

    # 用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数  958.137281791
    # It is used to evaluate whether the number of clusters is appropriate.
    # The smaller the distance, the better the cluster division.
    # The number of clusters at the critical point is selected
    print(clf.inertia_)

    ########################################################################
    #                               第二步 聚类GMM（太耗资源）
    '''
    print('Start GMM:')

    gmm = GaussianMixture(n_components=4).fit(weight)

    print(gmm)


    # print 'Start MiniBatchKmeans:'
    # from sklearn.cluster import MiniBatchKMeans
    # clf = MiniBatchKMeans(n_clusters=20)
    # s = clf.fit(weight)
    # print s


    # 中心点
    # print(clf.cluster_centers_)

    # 每个样本所属的簇
    # label2 = []  # 存储1000个类标 4个类
    label2 = gmm.predict(weight)



    # 用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数  958.137281791
    # print(clf.inertia_)
    ########################################################################
    #                               第二步 聚类DBSCAN(效果不佳)

    print('Start DBSCAN:')

    dbs = DBSCAN(eps=0.5, min_samples=3)  # 景区 动物 人物 国家
    dbs = dbs.fit(weight)
    print(dbs)


    # print 'Start MiniBatchKmeans:'
    # from sklearn.cluster import MiniBatchKMeans
    # clf = MiniBatchKMeans(n_clusters=20)
    # s = clf.fit(weight)
    # print s


    # 中心点
    # print(clf.cluster_centers_)

    # 每个样本所属的簇
    label1 = []  # 存储1000个类标 4个类
    print(dbs.labels_)
    i = 1
    while i <= len(dbs.labels_):
        print(i, dbs.labels_[i - 1])
        label1.append(dbs.labels_[i - 1])
        i = i + 1

    # 用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数  958.137281791
    # print(clf.inertia_)

    '''
    ########################################################################
    #                     Step3 Graphic output and dimensionality reduction

    pca = PCA(n_components=2)  # Two-dimensional output
    newData = pca.fit_transform(weight)  # N-dimensional output
    print(newData)
    print(len(newData))

    x1 = []
    y1 = []

    x2 = []
    y2 = []

    x3 = []
    y3 = []

    x4 = []
    y4 = []

    for index, value in enumerate(label):
        if value == 0:
            print(newData[index][0],newData[index][1])
            x1.append(newData[index][0])
            y1.append(newData[index][1])
        elif value == 1:
            print(newData[index][0], newData[index][1])
            x2.append(newData[index][0])
            y2.append(newData[index][1])
        elif value == 2:
            print(newData[index][0], newData[index][1])
            x3.append(newData[index][0])
            y3.append(newData[index][1])
        elif value == 3:
            print(newData[index][0], newData[index][1])
            x4.append(newData[index][0])
            y4.append(newData[index][1])

    # Four colors red green blue black
    path = os.path.join(os.path.dirname(__file__), 'cluster_1')
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    plt.rcParams['savefig.dpi'] = 300 # Picture pixel
    plt.rcParams['figure.dpi'] = 300 # Resolution
    plt.rcParams['font.sans-serif']=['SimHei']  # Used to display Chinese labels normally
    # 服务器上貌似还是不能很好地显示中文，于是：
    #myfont = FontProperties(fname='../msyh.ttc')
    plt.rcParams['axes.unicode_minus']=False  # Used to display the negative sign normally
    plt.plot(x1, y1, 'or')
    plt.plot(x2, y2, 'og')
    plt.plot(x3, y3, 'ob')
    plt.plot(x4, y4, 'ok')
    plt.title('Tf-idf特征聚类效果')
    plt.savefig('cluster_tfidf',dpi=300)
    plt.show()

    ########################################################################
    #                     Step4 Generate clustered text
    path = os.path.join('../weibo-master/', 'cluster_1')
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    clustername1 = "cluster1.txt"
    clustername2 = "cluster2.txt"
    clustername3 = "cluster3.txt"
    clustername4 = "cluster4.txt"
    cluster1 = codecs.open(clustername1, 'w', 'utf-8')
    cluster2 = codecs.open(clustername2, 'w', 'utf-8')
    cluster3 = codecs.open(clustername3, 'w', 'utf-8')
    cluster4 = codecs.open(clustername4, 'w', 'utf-8')

    for index, value in enumerate(label):
        #print(value,content_comment[index])
        if value == 0:
            print(value, content_comment[index][0])
            cluster1.write(content_comment[index][0] + '\n')
            cluster1.write(' ' + '\n')
        elif value == 1:
            print(value, content_comment[index][0])
            cluster2.write(content_comment[index][0] + '\n')
            cluster2.write(' ' + '\n')
        elif value == 2:
            print(value,content_comment[index][0])
            cluster3.write(content_comment[index][0] + '\n')
            cluster3.write(' ' + '\n')
        elif value == 3:
            print(value, content_comment[index][0])
            cluster4.write(content_comment[index][0] + '\n')
            cluster4.write(' ' + '\n')

    cluster1.close()
    cluster2.close()
    cluster3.close()
    cluster4.close()
