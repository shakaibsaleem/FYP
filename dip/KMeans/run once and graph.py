import random
import matplotlib.pyplot as plt

# takes a dict of clusters and plots them on a graph
def plotter(d,i):
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
	plt.title("Iteration: " + str(i))
	plt.axis([-1.1, 1.1, -1.1, 1.1])
	plt.savefig('Iteration' +  str(i) + '.png')
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
	count = 0
	stopIterations = False # Flag for terminating loop
	# Stops the algorithm when no significant changes in seeds
	while not stopIterations:
		count+=1
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
		plotter(clusters,count)
	print(count,"iterations")
	print('Images for each Iteration have been saved.')
	input("Press RETURN to exit")
# points = [(1,0),(0,1),(0,0),(7,7),(8,8),(10,10)]

points = []
def initializePoints(count):
	for i in range(int(count/3)+1):
		points.append([random.gauss(0,10),random.gauss(100,10)])
	for i in range(int(count/3)):
		points.append([random.gauss(-40,20),random.gauss(10,10)])
	for i in range(int(count/3)):
		points.append([random.gauss(40,20),random.gauss(10,10)])
initializePoints(1000)
k = 3
kMeans(points,k)
