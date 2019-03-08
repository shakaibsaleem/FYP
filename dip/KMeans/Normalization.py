import csv
# import os
# import shutil
# from pathlib import Path



def normalise(points):
    # global pointsDict
    # pointsDict contains normalised and original points as key value pairs (normalised are as key)
    # Takes a set of points, normalises them to a scale of -1 to 1 and returns as a list
    points = list(points)
    min1 = points[0][0]
    max1 = points[0][0]
    min2 = points[0][1]
    max2 = points[0][1]
    min3 = points[0][2]
    max3 = points[0][2]
    min4 = points[0][3]
    max4 = points[0][3]
    min5 = points[0][4]
    max5 = points[0][4]
    min6 = points[0][5]
    max6 = points[0][5]
    min7 = points[0][6]
    max7 = points[0][6]
    min8 = points[0][7]
    max8 = points[0][7]
    min9 = points[0][8]
    max9 = points[0][8]
    min10 = points[0][9]
    max10 = points[0][9]
    min11 = points[0][10]
    max11 = points[0][10]
    min12 = points[0][11]
    max12 = points[0][11]
    min13 = points[0][12]
    max13 = points[0][12]

    for i in range(len(points)):
        if points[i][0] < min1:
            min1 = points[i][0]
        if points[i][0] > max1:
            max1 = points[i][0]
            
        if points[i][1] < min2:
            min2 = points[i][1]
        if points[i][1] > max2:
            max2 = points[i][1]

        if points[i][2] < min3:
            min3 = points[i][2]
        if points[i][2] > max3:
            max3 = points[i][2]

        if points[i][3] < min4:
            min4 = points[i][3]
        if points[i][3] > max4:
            max4 = points[i][3]

        if points[i][4] < min5:
            min5 = points[i][4]
        if points[i][4] > max5:
            max5 = points[i][4]

        if points[i][5] < min6:
            min6 = points[i][5]
        if points[i][5] > max6:
            max6 = points[i][5]
            
        if points[i][6] < min7:
            min7 = points[i][6]
        if points[i][6] > max7:
            max7 = points[i][6]
            
        if points[i][7] < min8:
            min8 = points[i][7]
        if points[i][7] > max8:
            max8 = points[i][7]

        if points[i][8] < min9:
            min9 = points[i][8]
        if points[i][8] > max9:
            max9 = points[i][8]

        if points[i][9] < min10:
            min10 = points[i][9]
        if points[i][9] > max10:
            max10 = points[i][9]

        if points[i][10] < min11:
            min11 = points[i][10]
        if points[i][10] > max11:
            max11 = points[i][10]

        if points[i][11] < min12:
            min12 = points[i][11]
        if points[i][11] > max12:
            max12 = points[i][11]

        if points[i][12] < min13:
            min13 = points[i][12]
        if points[i][12] > max13:
            max13 = points[i][12]

        
    a3 = max(abs(min1),max1)
    b3 = max(abs(min2),max2)
    c3 = max(abs(min3),max3)
    d3 = max(abs(min4),max4)
    e3 = max(abs(min5),max5)
    f3 = max(abs(min6),max6)
    g3 = max(abs(min7),max7)
    h3 = max(abs(min8),max8)
    i3 = max(abs(min9),max9)
    j3 = max(abs(min10),max10)
    k3 = max(abs(min11),max11)
    l3 = max(abs(min12),max12)
    m3 = max(abs(min13),max13)

    newPoints = list()
    pointsDict = dict()
    # print(pointsDict)
    pNew = ()
    for p in points: # i dont think if this next line is correct. should divide all values by one value, the max of all maxes
        pNew = (p[0]/a3,p[1]/b3,p[2]/c3,p[3]/d3,p[4]/e3,p[5]/f3,p[6]/g3,p[7]/h3,p[8]/i3,p[9]/j3,p[10]/k3,p[11]/l3,p[12]/m3)
        newPoints.append(pNew)
        pointsDict[pNew] = p
    # print(newPoints)
    return newPoints

def getPoints(file):
    # gets points from csv file
    rd = csv.reader(open(file))
    names = []
    feats = []
    headers = []
    temp = []
    for row in rd:
        names.append(row[0])
        # headers.append(row[1])
        feats.append(row[1:])
    # print(names)
    for l in feats[1:]:
        temp.append([float(i) for i in l])
    names = names[1:]
    a = (normalise(temp))
    # print(feats)
    # for i in range(len(names)):
    writeList = []
    b =feats[0]
    b.insert(0,'filename')
    # print(b)
    writeList.append(b)
    for i in range(len(names)):
        # print())
        # print(i)
        q = list(a[i])
        q.insert(0,names[i])
        print(q)
        writeList.append(q)
    # for i in a:
    #     writeList.append(list(i))
    # print(writeList)
    with open(file[:-4] + 'normalized' + '.csv' , 'w', newline='') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(writeList)
    # print(temp)
    # newDict = dict()
    # for i in range(len(temp)):
    #     newDict[tuple(temp[i])] = names[i]
    # # print(newDict)
    # return temp,newDict
getPoints('haralick_no_human7_3 color.csv')
