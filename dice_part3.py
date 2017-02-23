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

n_rolls = 10000
n_events =  1000
n_bins=80
x_min = 0
x_max = 400

rolls1 = []
rolls2 = []
rolls3 = []
for n in range(n_rolls):
    if not n%1000:
        print n
    d1 = np.random.randint(1,high=9,size=20)
    d2 = np.random.randint(1,high=31,size=15)
    d3 = np.random.randint(1,high=151,size=2)
    rolls1.append(sum(d1))
    rolls2.append(sum(d2))
    rolls3.append(sum(d3))

sizes = [2, 6, 4]


# create dataset by drawing from sum of all distributions

data = []
for n in range(n_events):
    choice = np.random.randint(1,high=sum(sizes)+2)
    if choice <= sizes[0]:
        datum = np.random.randint(1,high=151,size=2)
    elif choice <= sizes[0]+sizes[1]:
        datum = np.random.randint(1,high=31,size=15)
    elif choice <= sizes[0]+sizes[1]+sizes[2]:
        datum = np.random.randint(1,high=9,size=20)
    else:
        datum = np.random.randint(1,high=5,size=55)


    data.append(sum(datum))

    if n>0 and (n+1)%5:
        continue
#    if n>99 and (n+1)%10:
#        continue
    
#    if n > 10:
#        break
    print n+1
#    if n < 9999:
#        continue

    y,binEdges=np.histogram(data,bins=n_bins,range=(x_min, x_max))
    bincenters = 0.5*(binEdges[1:]+binEdges[:-1])

    weights = [[size/float(sum(sizes)+1)]*n_rolls for size in sizes]
    new_weights = [[weight*(n+1)/float(n_rolls) for weight in weightset] for weightset in weights]


    plot = plt.hist([rolls3,rolls2,rolls1], n_bins, range=[x_min, x_max], histtype='stepfilled', weights=new_weights, stacked=True,
                    label=["2 150-sided dice, size 1","15 30-sided dice, size 3","20 8-sided dice, size 2"])

#    plot = plt.hist([rolls3,rolls2,rolls1], n_bins,range=[x_min, n_bins],histtype='step',weights=3*[weight],label=["10-sided dice","8-sided dice","6-sided dice"],linewidth=3)

    axes = plt.gca()
    axes.set_title("              "+str(n+1)+" rolls",y=0.55,fontsize=50)
    ymax = axes.get_ylim()[1]
#    axes.set_ylim([0,(n+1)/float(3.0)])
    axes.set_ylim([0,(n_events+1)/float(n_bins/6.)])
    axes.set_ylabel("events")
    axes.yaxis.set_label_coords(-0.07, 0.85)
#    axes.set_xlim(xmin=x_min+1, xmax=n_bins+1)
    axes.set_xlabel("sum of dice")
    axes.xaxis.set_label_coords(0.87, -0.05)

    data_plot = plt.plot(bincenters,y,'ko',label="data",markersize=10,markeredgewidth=0.0)
    leg = plt.legend(numpoints=1,fontsize=30)
    leg.draw_frame(False)

    plt.savefig('plot_'+str(n+1)+'.png')
    plt.cla()

