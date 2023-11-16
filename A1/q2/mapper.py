#!/usr/bin/env python
"""mapper.py"""

import sys

# get initial centroids from stdin and add them in an array
def getCentroids():
    centroids = []
    for line in sys.stdin:  
        # remove leading and trailing whitespace  
        line = line.strip()  
        # split the line into words  
        coor= line.split(',')  
        centroids.append([coor[0],coor[1]])
    return centroids

# create clusters based on initial centroids
def createClusters(centroids,filepath):
    '''
    Mapper function:
        load in coordinates, Centroid, 
        Calculate the distances from each sample to each centroid point
        output relabeled cluster ID as key, Coordinates as value.
    '''
    file = open(filepath, 'r')
    lines = file.readlines()
    for line in lines:  
        dist=99999.9
        cluster=-1
        line = line.strip()
        coor= line.split(',')
        xp,yp=float(coor[0]),float(coor[1])
        for i in range(len(centroids)):
            xc,yc=float(centroids[i][0]),float(centroids[i][1])
            dist_c=(xp-xc)**2+(yp-yc)**2
            if dist_c<dist:
                dist=dist_c
                cluster=i
        print ('%s\t%s,%s' % (cluster, xp,yp))

centroids = getCentroids()
createClusters(centroids,"./../data_points.txt")