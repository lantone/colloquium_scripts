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



n_rolls = 100000
n_events = 100
n_bins=17
x_min = 0

rolls1 = []
rolls2 = []
rolls3 = []
for n in range(n_rolls):
    d1 = np.random.randint(1,high=5,size=2)
    d2 = np.random.randint(1,high=7,size=2)
    d3 = np.random.randint(1,high=9,size=2)
    rolls1.append(sum(d1))
    rolls2.append(sum(d2))
    rolls3.append(sum(d3))

data = []
for n in range(n_events):
    datum = np.random.randint(1,high=7,size=2)
    data.append(sum(datum))
#    if n>0 and (n+1)%5:
#        continue
    print n

    y,binEdges=np.histogram(data,bins=n_bins,range=(x_min, n_bins))
    bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
    data_plot = plt.plot(bincenters,y,'ko',label="data")

    weight = [(n+1)/float(n_rolls)] * n_rolls
#    weight = [1] * n_rolls
    weights = [weight] * 3


    plot = plt.hist([rolls3,rolls2,rolls1], n_bins,range=[x_min, n_bins],histtype='step',weights=weights,label=["8-sided dice","6-sided dice","4-sided dice"])
    axes = plt.gca()
    axes.set_title(str(n+1)+" rolls",y=1.04,fontsize=30)
    ymax = axes.get_ylim()[1]
    axes.set_ylim([0,1.1*ymax])
    axes.set_ylabel("events")
#    axes.set_ylim([0,50])
    plt.legend(numpoints=1)
    plt.savefig('plot_'+str(n+1)+'.png')
    plt.cla()
#plot = plt.hist([rolls24,rolls6], n_bins,range=[0, n_bins])
#plot6 = plt.hist(rolls6, 20,range=[0, 20])
#plot24 = plt.hist(rolls24, 20,range=[0, 20])
#plt.show()
