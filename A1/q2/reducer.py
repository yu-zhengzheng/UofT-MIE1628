#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter  
import sys  

current_clus = '0'
xs,ys,count=0,0,0
  
# input comes from STDIN  
for line in sys.stdin:  
    # remove leading and trailing whitespace  
    line = line.strip()  
  
    # parse the input we got from mapper.py  
    cluster, coor = line.split('\t', 1)  
    x,y=coor.split(',',1)
    xs+=float(x)
    ys+=float(y)
    count+=1
    if current_clus!=cluster:
        print(xs/count,ys/count,sep=',')
        xs,ys,count=0,0,0
        current_clus=cluster

print(xs/count,ys/count,sep=',')
