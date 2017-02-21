#!/usr/bin/env python

import sys
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
fig_size[0] = 13
fig_size[1] = 10
plt.rcParams["figure.figsize"] = fig_size

plt.subplots_adjust(left=0.1,right=0.95, top=0.9, bottom=0.1)

n_rolls = 1000000
n_events = 1000
n_bins=21
x_min = 0

rolls1 = []
rolls2 = []
rolls3 = []
for n in range(n_rolls):
    d1 = np.random.randint(1,high=7,size=2)
    d2 = np.random.randint(1,high=9,size=2)
    d3 = np.random.randint(1,high=11,size=2)
    rolls1.append(sum(d1))
    rolls2.append(sum(d2))
    rolls3.append(sum(d3))

plot = plt.hist([rolls3,rolls2,rolls1], n_bins,range=[x_min, n_bins],histtype='step',label=["10-sided dice","8-sided dice","6-sided dice"],linewidth=3)
axes = plt.gca()
ymax = axes.get_ylim()[1]
axes.set_ylim([0,(n_rolls+1)/float(4)])
axes.set_ylabel("events")
axes.yaxis.set_label_coords(-0.07, 0.85)
axes.set_xlim(xmin=x_min+1, xmax=n_bins+1)
axes.set_xlabel("sum of two dice")
axes.xaxis.set_label_coords(0.87, -0.05)
leg = plt.legend(numpoints=1,loc=2,fontsize=30)
leg.draw_frame(False)
plt.savefig('plot_0.png')
plt.cla()

data = []
for n in range(n_events):
    datum = np.random.randint(1,high=9,size=2)
    data.append(sum(datum))
    if n>100 and (n+1)%10:
        continue

    print n+1
#    if n < 9999:
#        continue

    y,binEdges=np.histogram(data,bins=n_bins,range=(x_min, n_bins))
    bincenters = 0.5*(binEdges[1:]+binEdges[:-1])

    weight = [(n+1)/max(25.,float(n_rolls))] * n_rolls
#    weight = [1] * n_rolls

    plot = plt.hist([rolls3,rolls2,rolls1], n_bins,range=[x_min, n_bins],histtype='step',weights=3*[weight],label=["10-sided dice","8-sided dice","6-sided dice"],linewidth=3)

    axes = plt.gca()
    axes.set_title("                     "+str(n+1)+" rolls",y=0.85,fontsize=50)
    ymax = axes.get_ylim()[1]
    axes.set_ylim([0,max(25,(n+1)/float(4))])
    axes.set_ylabel("events")
    axes.yaxis.set_label_coords(-0.07, 0.85)
    axes.set_xlim(xmin=x_min+1, xmax=n_bins+1)
    axes.set_xlabel("sum of two dice")
    axes.xaxis.set_label_coords(0.87, -0.05)

    data_plot = plt.plot(bincenters,y,'ko',label="data",markersize=10,markeredgewidth=0.0)
    leg = plt.legend(numpoints=1,loc=2,fontsize=30)
    leg.draw_frame(False)

    plt.savefig('plot_'+str(n+1)+'.png')
    plt.cla()

