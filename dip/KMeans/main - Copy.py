import random
import matplotlib.pyplot as plt

# takes a dict of clusters and plots them on a graph
def plotter(d):
	keys = list(d.keys())
	colours=['red','green','blue','cyan','magenta','yellow','red','green','blue','cyan','magenta','yellow','red','green','blue','cyan','magenta','yellow','red','green','blue','cyan','magenta','yellow']
	for k in keys:
		ls = d[k]
		x,y = [],[]
		for point in ls:
			x.append(point[0])
			y.append(point[1])
		plt.plot(x,y,color=colours.pop(0),marker='+',linestyle='')
		plt.plot(k[0],k[1],color='black', marker='o',linestyle='')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.axis([-1.1, 1.1, -1.1, 1.1])
	plt.show()

def getDist(a,b):
	# returns euclidean distance from a to b
	(a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1,m1) = a
	(a2,b2,c2,d2,e2,f2,g2,h2,i2,j2,k2,l2,m2) = b
	return ((a1-a2)**2 + (b1-b2)**2 + (c1-c2)**2 + (d1-d2)**2 +(e1-e2)**2 +(f1-f2)**2 +(g1-g2)**2 +(h1-h2)**2 +(i1-i2)**2 +(j1-j2)**2 +(k1-k2)**2 +(l1-l2)**2 + (m1-m2)**2)**0.5

def getClosestSeed(point,seeds):
	# Take a (x,y) pair as point and seeds is a list of seed points
	# Returs (x,y) pair, a seed from given seeds, which is closest to the given point
	minDist = -1
	closestPoint = (0,0,0,0,0,0,0,0,0,0,0,0,0)
	for seed in seeds:
		dist = getDist(point,seed)
		if dist < minDist or minDist==-1: # always update minDist in first run
			# replace previous min with current
			minDist = dist
			closestPoint = seed
	return closestPoint

def getMeanPoint(ls):
	# Takes a list of (x,y) points
	# Returns a point (x,y) that is the mean of all given points
	if len(ls) == 0:
		return (0,0,0,0,0,0,0,0,0,0,0,0,0)
	suma, sumb,sumc, sumd,sume, sumf,sumg, sumh,sumi, sumj,sumk, suml,summ  = 0,0,0,0,0,0,0,0,0,0,0,0,0
	for point in ls:
		suma += point[0]
		sumb += point[1]
		sumc += point[2]
		sumd += point[3]
		sume += point[4]
		sumf += point[5]
		sumg += point[6]
		sumh += point[7]
		sumi += point[8]
		sumj += point[9]
		sumk += point[10]
		suml += point[11]
		summ += point[12]
	a = suma/len(ls)
	b = sumb/len(ls)
        c = sumc/len(ls)
	d = sumd/len(ls)
        e = sume/len(ls)
	f = sumf/len(ls)
        g = sumg/len(ls)
	h = sumh/len(ls)
        i = sumi/len(ls)
	j = sumj/len(ls)
        k = sumk/len(ls)
	l = suml/len(ls)
        m = summ/len(ls)
	
	return (a,b,c,d,e,f,g,h,i,j,k,l,m)

def areSeedsChanging(oldSeeds,newSeeds):
	# Returns True if any changes in Seeds
	if set(oldSeeds)==set(newSeeds):
		return False
	else:
		return True

def normalise(points):
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
	for p in points:
		newPoints.append(p[0]/a3,p[1]/b3,p[2]/c3,p[3]/d3,p[4]/e3,p[5]/f3,p[6]/g3,p[7]/h3,p[8]/i3,p[9]/j3,p[10]/k3,p[11]/l3,p[12]/m3)
	return newPoints

def kMeans(points,k):
	data = normalise(points)

	# Initialising seed points
	seeds = set() # to avoid dublicates
	while len(seeds) < k: # genreating k number of seeds

		# Generating a random number between [-1,1)
		a = random.random()*2-1
		b = random.random()*2-1
        c = random.random()*2-1
		d = random.random()*2-1
        e = random.random()*2-1
		f = random.random()*2-1
        g = random.random()*2-1
		h = random.random()*2-1
        i = random.random()*2-1
		j = random.random()*2-1
        k = random.random()*2-1
		l = random.random()*2-1
        m = random.random()*2-1

		seeds.add((a,b,c,d,e,f,g,h,i,j,k,l,m))
	seeds = list(seeds) # convering in order to support indexing

	# Stops the algorithm when no significant changes in seeds
	stopIterations = False # Flag for terminating loop
	while not stopIterations:

		# Creating a dictionary of clusters with current seeds as each index
		clusters = dict()
		for i in range(k):
			clusters[seeds[i]] = list() # each cluster is a list, initially empty

		# Updating clusters based on current seeds
		for point in data:
			seed = getClosestSeed(point,seeds)
			clusters[seed].append(point)

		# Updating seed points based on current clusters
		newSeeds = list()
		for seed in seeds:
			meanPoint = getMeanPoint(clusters[seed])
			newSeeds.append(meanPoint)
		stopIterations = not areSeedsChanging(seeds,newSeeds)
		seeds = newSeeds
	return clusters

def initializePoints(count):
	points = []
	for i in range(int(count/3)):
		points.append([random.gauss(0,10),random.gauss(100,10)])
	for i in range(int(count/4)):
		points.append([random.gauss(-30,20),random.gauss(10,10)])
	for i in range(int(count/4)):
		points.append([random.gauss(30,20),random.gauss(10,10)])
	return points

def quality(clusters):
	centroids = list(clusters.keys())
	intra_cluster_dist = 0
	for centroid in centroids:
		points = clusters[centroid]
		for point in points:
			intra_cluster_dist += getDist(point,centroid)
	inter_cluster_dist = 0
	for i in range(len(centroids)):
		for j in range(i+1):
			inter_cluster_dist += getDist(centroids[i],centroids[j])
	return (intra_cluster_dist,inter_cluster_dist)

def getBestResult(results):
	inter_list = list()
	intra_list = list()
	max_intra = 0
	min_intra = float("inf")
	max_inter = 0
	for result in results:
		intra_cluster_dist, inter_cluster_dist = quality(result)
		inter_list.append(inter_cluster_dist)
		intra_list.append(intra_cluster_dist)
		if intra_cluster_dist > max_intra:
			max_intra = intra_cluster_dist
		if intra_cluster_dist < min_intra:
			min_intra = intra_cluster_dist
		if inter_cluster_dist > max_inter:
			max_inter = inter_cluster_dist
	best_score = 0
	for i in range(len(results)):
		inter_score = inter_list[i]/max_inter
		intra_score = 1 - intra_list[i]/max_intra
		score = inter_score + intra_score
		if score > best_score:
			best_score = score
			best_result = results[i]
	return best_result

def main():
	results = list()
	points = initializePoints(1000)
	k = 3
	for i in range(10):
		clusters = kMeans(points, k)
		results.append(clusters)
	bestResult = getBestResult(results)
	plotter(bestResult)

main()