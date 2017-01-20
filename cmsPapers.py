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
matplotlib.rcParams.update({'font.size': 40})
plt.subplots_adjust(top=0.97,bottom=0.15,right=0.95)

groups = ('BSM', 'SM', 'Higgs', 'HI')
y_pos = np.arange(len(groups))
#        EXO, SM, Higgs, HI
papers = (114, 96, 69, 54)
#        SUSY,Top
papers2 = (73,67,0,0)
#        B2G
papers3 = (20,0,0,0)

#D62724 -red
#FE7F0D -orange
#BDBD27 -yellow
#2AA028 -green
#1F78B4 -blue
#9064BD -purple
#8C564A -brown

plot=plt.barh(y_pos, papers, align='center', alpha=0.8,edgecolor = "none",linewidth=0)
plot[0].set_color('#1F78B4')#EXO
plot[1].set_color('#FE7F0D')#SM
plot[2].set_color('#D62724')#Higgs
plot[3].set_color('#8C564A')#HI

plot2=plt.barh(y_pos, papers2, left=papers, align='center', alpha=0.8,edgecolor = "none",linewidth=0)
plot2[0].set_color('#2AA028')#SUSY
plot2[1].set_color('#9064BD')#Top
plot2[2].set_color('none')
plot2[3].set_color('none')

plot3=plt.barh(y_pos, papers3, left=[i+j for i,j in zip(papers,papers2)], align='center', alpha=0.8,edgecolor = "none",linewidth=0)
plot3[0].set_color('#BDBD27')#B2G
plot3[1].set_color('none')
plot3[2].set_color('none')
plot3[3].set_color('none')

plt.yticks(y_pos, groups)
plt.xlabel('Number of papers')
plt.show()



