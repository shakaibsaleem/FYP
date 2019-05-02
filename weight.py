import Kmeans
import csv
import statistics
from itertools import combinations 


def Quality(n):
	file = 'haralick_no_human7_3 colornormalized.csv'
	haralick_dict = {}
	rd = csv.reader(open(file))

	for row in rd:
		haralick_dict[row[0]] = list((row[1:]))

	a = Kmeans.main(file,n)
	centroid = []
	elements_in_cluster = []
	for i in a:
		# print(i)
		cluster_mean = []
		for j in range(13):
			temp1 = [float(haralick_dict[z][j]) for z in i]
			# print(temp1)0.06774464759494403
			temp = statistics.mean(temp1)
			cluster_mean.append(temp)
		centroid.append(cluster_mean)
		elements_in_cluster.append(len(i))
		# ll.append(cluster_mean)

	# print('c',len(centroid))

	def getDist(a,b):
	    # returns euclidean distance from a to b
	    a = map(float,a)
	    b = map(float,b)
	    (a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1,m1) = a
	    (a2,b2,c2,d2,e2,f2,g2,h2,i2,j2,k2,l2,m2) = b
	    return ((a1-a2)**2 + (b1-b2)**2 + (c1-c2)**2 + (d1-d2)**2 +(e1-e2)**2 +(f1-f2)**2 +(g1-g2)**2 +(h1-h2)**2 +(i1-i2)**2 +(j1-j2)**2 +(k1-k2)**2 +(l1-l2)**2 + (m1-m2)**2)**0.5

	def getRS(a):
	    a = map(float,a)
	    SqSum = 0
	    for i in a:
	    	SqSum = SqSum + (i**2)

	    return SqSum**0.5

	distance_centroid = []
	for i in range(7):
		temp = []
		for j in a[i]:
			temp.append(getDist(haralick_dict[j],centroid[i]))
		distance_centroid.append(temp)

	Intra_quality = []
	for i in distance_centroid:
		Intra_quality.append(getRS(i))

	print(Intra_quality)
	def WeightedMean(a,b):
		return (sum([x*y for x,y in zip(a,b)]))/sum(b)


	print('intra cluster quality' , WeightedMean(Intra_quality,elements_in_cluster))
	# print('Intra_quality', Intra_quality)



	comb = combinations(centroid, 2) 
	  
	list_comb = (list(comb))
	inter_distances = []

	for i in list_comb:
		inter_distances.append(getDist(i[0],i[1]))


	print(inter_distances)
	print('inter cluster quality',statistics.mean(inter_distances))


Quality(7)