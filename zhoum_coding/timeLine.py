#coding:utf8

def plotCountsPerSpeedZone(data,controller = 50):
    import matplotlib.pyplot as plt
    data = data[['TERMINALNO','TRIP_ID','TIME','SPEED']]
    # data = data[data['TERMINALNO'] == 1]
    time = data.TIME
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