#coding:utf8
author = "zhouming"

import pandas as pd
import pickle as pkl
import matplotlib.pyplot as plt
import time
from sklearn import preprocessing

#转源数据为pkl文件
# pd.read_csv("../PINGAN-2018-train_demo.csv",sep = ",").to_pickle("./PINGAN-2018-train_demo.pkl")
data = pd.read_pickle("./PINGAN-2018-train_demo.pkl")
data.drop_duplicates(inplace = True)#经查验无重复
'''
属性介绍：
TERMINALNO, 用户id：用户唯一标志
TIME,       unix时间戳：从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数，不考虑闰秒
TRIP_ID,    行程id：用户行程唯一标志
LONGITUDE,  经度：用户行程目前所在经度
LATITUDE,   纬度：用户行程目前所在维度
DIRECTION,  方向(角度)：用户行程目前对应方向，正北为0，顺时针方向计算角度（如正东为90、正南为180），负值代表此时方向不可判断
HEIGHT,     海拔(m)：用户行程目前所处的海拔高度
SPEED,      速度(km/h)：用户行程目前的速度
CALLSTATE,  电话状态：用户行程目前的通话状态。（0,未知 1,呼出 2,呼入 3,连通 4,断连）
Y           客户赔付率：客户赔付情况，为本次建模的目标Y值。（test中不含此字段）
'''
data.TIME = data.TIME.map(lambda x:time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(x)))

#100个TERMINALNO，223个TRIP_ID
# print(data.TERMINALNO.value_counts())
# print(data.TRIP_ID.value_counts())

#初步思路：速度、加速度、时间变化图
#某辆行程的加速度变化图

data.sort_values(by=['TERMINALNO','TRIP_ID','TIME'],ascending=[0,1,2],inplace=True)
data = data[['TERMINALNO','TRIP_ID','TIME','SPEED']]
# data = data[data['TERMINALNO'] == 1]
time = data.TIME
speed = data.SPEED


# tmp = pd.DataFrame({u'time':time,u'speed':speed})
plt.figure()
plt.scatter(time, speed)
plt.grid(True)
plt.xticks()
plt.xlabel('time')
plt.ylabel('speed')
plt.title('time_speed')
plt.show()