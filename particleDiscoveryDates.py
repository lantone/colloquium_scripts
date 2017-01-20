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
matplotlib.rcParams.update({'font.size': 22})


# python dictionary containing mass and discovery date for each fundamental particle

# structure: 
#  key = short name
#  'mass' = mass in GeV
#  'year' = year of discovery

particleData = {
    'e' : {
        'mass' : 0.000511,
        'year' : 1897, # thompson
     },
    'mu' : {
        'mass' : 0.106,
        'year' : 1936,
     },
    'tau' : {
        'mass' : 1.777,
        'year' : 1975,
     },
     'nu_e' : {
         'mass' : 0,
         'year' : 1956, 
      },
     'nu_mu' : {
         'mass' : 0,
         'year' : 1962,
      },
     'nu_tau' : {
         'mass' : 0,
         'year' : 2000,
      },
    'u' : {
        'mass' : 0.0023,
        'year' : 1968,
     },
    'd' : {
        'mass' : 0.0048,
        'year' : 1968,
     },
    's' : {
        'mass' : 0.095,
        'year' : 1968,
     },
    'c' : {
        'mass' : 1.275,
        'year' : 1974,
     },
    'b' : {
        'mass' : 4.18,
        'year' : 1977,
     },
    't' : {
        'mass' : 173,
        'year' : 1995,
     },
     'p' : {
         'mass' : 0,
         'year' : 1905,
      },
     'g' : {
         'mass' : 0,
         'year' : 1978,
      },
    'w' : {
        'mass' : 80.4,
        'year' : 1983,
     },
    'z' : {
        'mass' : 91.2,
        'year' : 1983,
     },
     'h' : {
         'mass' : 125.1,
         'year' : 2012,
      },
}



x = []
y = []
for particle,data in particleData.iteritems():
    x.append(data['year'])
    y.append(data['mass'])

fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 8
fig_size[1] = 8
plt.rcParams["figure.figsize"] = fig_size
plt.subplots_adjust(left=0.15)
    
plt.yscale('log')
plt.scatter(x, y,s=2)
plt.gca().set_xlim(1960, 2020)
plt.gca().set_ylim(0.05, 1000)
plt.xlabel('Discovery Year')
plt.ylabel('Particle Mass (GeV)')
import matplotlib.ticker as ticker
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda y,pos: ('{{:.{:1d}f}}'.format(int(np.maximum(-np.log10(y),0)))).format(y)))


from scipy.optimize import curve_fit
def func(x, a, b, c):
    return a*x**3 + b*x**2 +c*x

#plt.legend()
#plt.plot(np.unique(x_fit), np.poly1d(np.polyfit(x_fit, y_fit, 1))(np.unique(x_fit)),'r-')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['right'].set_color('none')
plt.gca().xaxis.set_ticks_position('bottom')
plt.gca().yaxis.set_ticks_position('left')



x_fit = (1968,1974,1977,1983,1983)
y_fit = (0.095,1.275,4.18,80,91)
x = np.array(x_fit, dtype=float)
y = np.array(y_fit, dtype=float)
popt, pcov = curve_fit(func, x, y)
#print popt, pcov
#print "a = %s , b = %s, c = %s" % (popt[0], popt[1], popt[2])
#plt.plot(x, func(x, *popt), 'r-', label="Fitted Curve")


plt.show()

