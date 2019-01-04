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
	(x1,y1) = a
	(x2,y2) = b
	return ((x1-x2)**2 + (y1-y2)**2)**0.5

def getClosestSeed(point,seeds):
	# Take a (x,y) pair as point and seeds is a list of seed points
	# Returs (x,y) pair, a seed from given seeds, which is closest to the given point
	minDist = -1
	closestPoint = (0,0)
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
		return (0,0)
	sumx, sumy = 0, 0
	for point in ls:
		sumx += point[0]
		sumy += point[1]
	x = sumx/len(ls)
	y = sumy/len(ls)
	return (x,y)

def areSeedsChanging(oldSeeds,newSeeds):
	# Returns True if any changes in Seeds
	if set(oldSeeds)==set(newSeeds):
		return False
	else:
		return True

def normalise(points):
	# Takes a set of points, normalises them to a scale of -1 to 1 and returns as a list
	points = list(points)
	minX = points[0][0]
	maxX = points[0][0]
	minY = points[0][1]
	maxY = points[0][1]

	for i in range(len(points)):
		if points[i][0] < minX:
			minX = points[i][0]
		if points[i][0] > maxX:
			maxX = points[i][0]
		if points[i][1] < minY:
			minY = points[i][1]
		if points[i][1] > maxY:
			maxY = points[i][1]
	x = max(abs(minX),maxX)
	y = max(abs(minY),maxY)

	newPoints = list()
	for p in points:
		newPoints.append((p[0]/x,p[1]/y))
	return newPoints

def kMeans(points,k):
	data = normalise(points)

	# Initialising seed points
	seeds = set() # to avoid dublicates
	while len(seeds) < k: # genreating k number of seeds

		# Generating a random number between [-1,1)
		x = random.random()*2-1
		y = random.random()*2-1
		seeds.add((x,y))
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
