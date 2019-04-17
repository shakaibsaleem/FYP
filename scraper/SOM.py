from __future__ import division

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import patches as patches
import csv
import os
from pathlib import Path
import shutil

# this code has been incorporated from http://blog.yhat.com/posts/self-organizing-maps-2.html

PointDictionary = dict()
def ge1tPoints(file):
    # gets points from csv file
    rd = csv.reader(open(file))
    names = []
    feats = []
    temp = []
    vectorlist = []
    for row in rd:
        names.append(row[0])
        feats.append(row[1:])
    for l in feats[1:]:
        temp.append([float(i) for i in l])

    names = names[1:]
    newDict = dict()
    for i in range(len(temp)):
        newDict[tuple(temp[i])] = names[i]
    # return temp,newDict
    for i in newDict:
        vectorlist.append(list(i))
    
    vectorlistnp = np.array(vectorlist)
    vectorarray = vectorlistnp.T
    for i in range(len(vectorlistnp)):
    	templist = []
    	for j in vectorlistnp[i]:
    		templist.append((j))
    	PointDictionary[str(templist)] = names[i]
    # print(vectorarray)
    return vectorarray





raw_data = ge1tPoints('haralick_no_human_grayscalenormalized.csv')


network_dimensions = np.array([3, 3])
n_iterations = 100000
init_learning_rate = 0.01

normalise_data = False
normalise_by_column = False

# print(raw_data)
m = raw_data.shape[0]
# print(m)
n = raw_data.shape[1]
# print(n)

# initial neighbourhood radius
init_radius = max(network_dimensions[0], network_dimensions[1]) / 2
# radius decay parameter
time_constant = n_iterations / np.log(init_radius)

data = raw_data

if normalise_data:
    if normalise_by_column:
        col_maxes = raw_data.max(axis=0)
        print(col_maxes)
        data = raw_data / col_maxes[np.newaxis, :]
        # print('data',raw_data)
        # print('nordata',data)
    else:
        data = raw_data / data.max()

net = np.random.random((network_dimensions[0], network_dimensions[1], m))


def find_bmu(t, net, m):
    """
        Find the best matching unit for a given vector, t
        Returns: bmu and bmu_idx is the index of this vector in the SOM
    """
    bmu_idx = np.array([0, 0])
    min_dist = np.iinfo(np.int).max
    
    # calculate the distance between each neuron and the input
    for x in range(net.shape[0]):
        for y in range(net.shape[1]):
            w = net[x, y, :].reshape(m, 1)
            sq_dist = np.sum((w - t) ** 2)
            sq_dist = np.sqrt(sq_dist)
            if sq_dist < min_dist:
                min_dist = sq_dist # dist
                bmu_idx = np.array([x, y]) # id
    
    bmu = net[bmu_idx[0], bmu_idx[1], :].reshape(m, 1)
    # print('bmu', (bmu, bmu_idx) )
    return (bmu, bmu_idx)


def decay_radius(initial_radius, i, time_constant):
    return initial_radius * np.exp(-i / time_constant)

def decay_learning_rate(initial_learning_rate, i, n_iterations):
    return initial_learning_rate * np.exp(-i / n_iterations)

def calculate_influence(distance, radius):
    return np.exp(-distance / (2* (radius**2)))

diction = {}

count = 0
for i in range(n_iterations):
    # select a training example at random    
    count += 1
    t = data[:, np.random.randint(0, n)].reshape(np.array([m, 1]))
    # print('t',t)
    # for i in t:
    # 	print(i)
    # 	print(type(i))

    # # print('yaha')
    # print(t)
    # print(type(t))
	    
    # find its Best Matching Unit
    bmu, bmu_idx = find_bmu(t, net, m)
    

    tt= []
    for i in t:
    	for j in i:
    		tt.append(j)
    diction[str(tt)] = str(bmu_idx)
    # print(t,'index',bmu_idx)
    # decay the SOM parameters
    r = decay_radius(init_radius, i, time_constant)
    l = decay_learning_rate(init_learning_rate, i, n_iterations)
    
    # update weight vector to move closer to input
    # and move its neighbours in 2-D vector space closer
    
    for x in range(net.shape[0]):
        for y in range(net.shape[1]):
            w = net[x, y, :].reshape(m, 1)
            w_dist = np.sum((np.array([x, y]) - bmu_idx) ** 2)
            w_dist = np.sqrt(w_dist)
            
            if w_dist <= r:
                # calculate the degree of influence (based on the 2-D distance)
                influence = calculate_influence(w_dist, r)
                # print(influence)
                # new w = old w + (learning rate * influence * delta)
                # where delta = input vector (t) - old w
                new_w = w + (l * influence * (t - w))
                net[x, y, :] = new_w.reshape(1, 13)
# NameClus = {}
# print(diction)
# print((PointDictionary))
# for key, value in PointDictionary.items():
# 	NameClus[key] = str(diction[value])

classes = []
for x,y in diction.items():
	classes.append(y)

classes = set(classes)
c=[]
for i in classes:
	temp = [PointDictionary[x] for x,y in diction.items() if y == i]
	c.append(temp)
# for k , v in (diction.items()):
# 	# print('k',k)
# 	# print('v',v)
# 	temp = []

# 	for x,y in PointDictionary.items():
# 		if y == k:
# 			temp.append(x)

# 	c[v] = temp

	# c[v] = [x for x,y in (PointDictionary.items()) if y==k ]

# print(c)

def folderDist(resultList,m,n):
    searchPath = 'C:/Users/Alizar/Documents/GitHub/FYP/dip/KMeans/No_Human'
    newpa = "C:/Users/Alizar/Documents/GitHub/FYP/dip/SOM/NoHumanClassification"
    num = 0
    print('result List', resultList)

    for i in resultList:
    	num += 1
    	newpath = newpa + 'ClustersN' + str(m) + '_' +str(n) + 'Label'+str(num)
    	try:
    		os.mkdir(newpath)
    	except OSError:
    		print ("Creation of the directory %s failed" % newpath)
    	else:
    		print ("Successfully created the directory %s " % newpath)

    	for j in i:
    		# print('entered')
    		# if j in os.path.isdir(searchPath):
    		# 	shutil.copy2(searchPath + j , str(path ++ j))
    		imgFile = Path(searchPath + '/' + j)
    		# print(imgFile)
    		if imgFile.is_file():
    			# print('yaha')
    			shutil.copy2(searchPath + '/' + j , newpath + '/' + j)


folderDist(c,network_dimensions[0],network_dimensions[1])
