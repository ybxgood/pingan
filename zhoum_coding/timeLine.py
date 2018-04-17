#coding:utf8

#速度按照区间划分
def plotCountsPerSpeedZone(data,controller = 50):
    import matplotlib.pyplot as plt
    data = data[['TERMINALNO','TRIP_ID','TIME','SPEED']]
    # data = data[data['TERMINALNO'] == 1]
    speed = data.SPEED
    sep = (max(speed) - min(speed))/controller
    speedZone = []

    initSpeed = min(speed)
    for i in range(controller):
        initSpeed += sep
        speedZone.append(int(initSpeed))
    countSpeedZone = []
    for i in range(controller - 1):
        countSpeedZone.append(len(data[(data.SPEED >= speedZone[i]) & (data.SPEED <= speedZone[i + 1])]))
    speedZone = speedZone[1:]
    plt.bar(speedZone,countSpeedZone,label = 'countsPerSpeedZone')
    plt.grid(True)
    # plt.xticks(speedZone)
    # plt.yticks(countSpeedZone)
    plt.xlabel('speedZone')
    plt.ylabel('counts')
    plt.title('countsPerSpeedZone')
    plt.show()

#时间按照区间划分
def plotCountsPerTimeZone(data,controller = 50):
    import matplotlib.pyplot as plt
    data = data[['TERMINALNO', 'TRIP_ID', 'TIME', 'SPEED']]
    # data = data[data['TERMINALNO'] == 1]
    times = data.TIME
    sep = (max(times) - min(times)) / 50
    timeZone = []

    initTime = min(times)
    for i in range(50):
        initTime += sep
        timeZone.append(int(initTime))
    countTimeZone = []
    for i in range(50 - 1):
        countTimeZone.append(len(data[(data.TIME >= timeZone[i]) & (data.TIME <= timeZone[i + 1])]))
    timeZone = timeZone[1:]
    plt.bar(timeZone, countTimeZone, label='countsPerTimeZone')
    plt.grid(True)
    # plt.xticks(speedZone)
    # plt.yticks(countSpeedZone)
    plt.xlabel('speedZone')
    plt.ylabel('counts')
    plt.title('countsPerSpeedZone')
    plt.show()

#打印时间分布特点
def timeMap(data):
    import pandas as pd
    import time
    year = []
    month = []
    data.TIME = data.TIME.map(lambda x: time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(x)))
    print(len(data.TIME))
    for i in range(len(data.TIME)):
        times = data.TIME[i]
        year.append(times[0:4])
        month.append(times[5:7])
    year = pd.Series(year)
    month = pd.Series(month)
    print(year.value_counts())
    print(month.value_counts())
