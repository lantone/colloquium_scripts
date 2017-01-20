#!/usr/bin/env python

#import sys
#import glob
#import re
#import os
#from array import *

import matplotlib
matplotlib.use('QT4Agg')

import numpy as np
import matplotlib.pyplot as plt
plt.xkcd()
matplotlib.rcParams.update({'font.size': 28})


fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 17
fig_size[1] = 10
plt.rcParams["figure.figsize"] = fig_size

plt.subplots_adjust(left=0.1,right=0.95, top=0.9, bottom=0.05)



n_rolls = 10000
n_events = 1000
n_bins=70
x_min = 0
x_max = 350

rolls1 = []
rolls2 = []
rolls3 = []
for n in range(n_rolls):
    d1 = np.random.randint(1,high=8,size=20)
    d2 = np.random.randint(1,high=30,size=15)
    d3 = np.random.randint(1,high=150,size=2)
    rolls1.append(sum(d1))
    rolls2.append(sum(d2))
    rolls3.append(sum(d3))

data = []
for n in range(n_events):
    choice = np.random.randint(1,high=7)
    if choice <= 1:
        datum = np.random.randint(1,high=150,size=2)
    elif choice <= 4:
        datum = np.random.randint(1,high=30,size=15)
    else:
        datum = np.random.randint(1,high=8,size=20)

    data.append(sum(datum))
    if n>0 and (n+1)%10:
        continue
    print n

    y,binEdges=np.histogram(data,bins=n_bins,range=(x_min, x_max))
    bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
    data_plot = plt.plot(bincenters,y,'ko',label="data")

    weight = [(n+1)/float(n_rolls)] * n_rolls
#    weight = [1] * n_rolls
    weights = [[x * 1/6. for x in weight],[x * 3/6. for x in weight],[x * 2/6. for x in weight]]
#    print n
#    print weights

    plot = plt.hist([rolls3,rolls2,rolls1], n_bins,range=[x_min, x_max],histtype='stepfilled',weights=weights,label=["bag of 2 150-sided dice, size 1","bag of 15 30-sided dice, size 3","bag of 20 8-sided dice, size2"],stacked=True)
    axes = plt.gca()
    axes.set_title(str(n+1)+" rolls",y=1.04,fontsize=30)
    ymax = axes.get_ylim()[1]
    axes.set_ylabel("events")
#    axes.set_ylim([0,1.1*ymax])
    axes.set_ylim([0,100])
    plt.legend(numpoints=1)
    plt.savefig('plot_'+str(n+1)+'.png')
    plt.cla()
#plot = plt.hist([rolls24,rolls6], n_bins,range=[0, n_bins])
#plot6 = plt.hist(rolls6, 20,range=[0, 20])
#plot24 = plt.hist(rolls24, 20,range=[0, 20])
#plt.show()
