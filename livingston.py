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
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
plt.xkcd()
matplotlib.rcParams.update({'font.size': 28})


fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 17
fig_size[1] = 10
plt.rcParams["figure.figsize"] = fig_size


host = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(left=0.05,right=0.8, top=0.95, bottom=0.05)

par1 = host.twinx()
par2 = host.twinx()

offset = 120
new_fixed_axis2 = par2.get_grid_helper().new_fixed_axis
par2.axis["right"] = new_fixed_axis2(loc="right",
                                    axes=par2,
                                    offset=(offset, 0))
par2.axis["right"].toggle(all=True)



#host.set_xlim(0, 2)
#host.set_ylim(0, 2)

energy_times = (2010.4, 2011.99, 2012.01, 2013.9, 2014.1, 2020.49, 2020.5, 2024)
energies =     (     7,       7,       8,       8,   13,     13,   14,   14)

years1 = (2010.5, 2011.5, 2012.5, 2015.5, 2016.5, 2017.5, 2018.5, 2021.5, 2022.5, 2023.5)
# in Hz/nb (10^33)
rate =  (    0.2,    4.0,    7.7,    5.0,     15,   17.5,   17.5,   18.5,     20,     20)
# in 1/fb
years2 = (2010.4, 2012, 2013.2, 2015.45, 2016, 2017, 2018, 2019, 2021, 2022, 2024)
data =   (     0,  5.5,   28.8,    28.8,   33,   73,  100,  140,  140,  190,  300)

#bar chart for shutdowns
years3 = (2013)
years4 = (2019)
shutdowns = (10000)

host.set_ylabel("Energy (TeV)")
par1.set_ylabel("Data Rate (Hz/nb)")
par2.set_ylabel("Total Data (1/fb)")

p1, = host.plot(energy_times, energies, 'g-',lw=15, label="Energy")
p2, = par1.plot(years1, rate, 'ro', ms=15, label="Data Rate")
p3, = par2.plot(years2, data, 'b-', lw=15, label="Total Data")
p4, = par2.bar(years3, shutdowns, 2, color='wheat',label="Shutdowns")
p5, = par2.bar(years4, shutdowns, 2, color='wheat')
p2.set_zorder(18)
p4.set_zorder(19)
p5.set_zorder(20)

ax = plt.gca()
ax.get_xaxis().get_major_formatter().set_useOffset(False)
ax.get_xaxis().get_major_formatter().set_scientific(False)
ax.autoscale_view()
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end))

host.set_ylim(0, 15)
par1.set_ylim(0, 25)
par2.set_ylim(0, 400)
host.set_xlim(2010, 2024)

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right"].label.set_color(p3.get_color())

host.axis["left"].major_ticklabels.set_color(p1.get_color())
par1.axis["right"].major_ticklabels.set_color(p2.get_color())
par2.axis["right"].major_ticklabels.set_color(p3.get_color())

host.axis["left"].line.set_color(p1.get_color())
host.axis["right"].line.set_color(p2.get_color())
par2.axis["right"].line.set_color(p3.get_color())

host.axis["left"].major_ticks.set_color(p1.get_color())
par1.axis["right"].major_ticks.set_color(p2.get_color())
par2.axis["right"].major_ticks.set_color(p3.get_color())





#handles, labels = host.get_legend_handles_labels()
#host.legend(handles[::-1], labels[::-1],loc=2,fontsize='medium')
leg = host.legend(loc=2,fontsize='medium')
leg.set_zorder(21)
plt.draw()
plt.show()
