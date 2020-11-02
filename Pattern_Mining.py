#%pylab
#begin import from course
#%matplotlib inline
import math
import scipy.stats as stats
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#end import from course

from collections import defaultdict
from scipy.stats.stats import pearsonr
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from pandas.plotting import parallel_coordinates

# Any results you write to the current directory are saved as output.

dfb = pd.read_csv("HR_comma_sep.csv")

#figsize(15, 10)#graphs size

import fim
from fim import apriori
#http://www.borgelt.net/pyfim.html

level=dfb['satisfaction_level'].values
time=dfb['last_evaluation'].values
hours=dfb['average_montly_hours'].values

min_lvl=min(level)
max_lvl=max(level)
bin_lvl= 10

min_evl=min(time)
max_evl=max(time)
bin_evl=10

min_h=min(hours)
max_h=max(hours)
bin_h=10

baskets = defaultdict(list)

for i in range(len(dfb)):
    
    #baskets[i].append(item_id)
    binsize=(max_lvl-min_lvl)/bin_lvl
    binnumber=int((dfb['satisfaction_level'][i]-min_lvl)/binsize)    
    baskets[i].append(str(binnumber*binsize+min_lvl)+'-'+str((binnumber+1)*binsize+min_lvl)+'_S')    
    
    binsize=(max_evl-min_evl)/bin_evl
    binnumber=int((dfb['last_evaluation'][i]-min_evl)/binsize)    
    baskets[i].append(str(binnumber*binsize+min_evl)+'-'+str((binnumber+1)*binsize+min_evl)+'_E')    
    
    binsize=(max_h-min_h)/bin_h
    binnumber=int((dfb['average_montly_hours'][i]-min_h)/binsize)    
    baskets[i].append(str(binnumber*binsize+min_h)+'-'+str((binnumber+1)*binsize+min_h)+'_A')
    
    baskets[i].append(str(dfb['number_project'][i])+'_N')
    baskets[i].append(str(dfb['time_spend_company'][i])+'_T')
    
    baskets[i].append(str(dfb['Work_accident'][i])+'_W')#genera molte regole poco significative
    baskets[i].append(str(dfb['left'][i])+'_L')
    baskets[i].append(str(dfb['promotion_last_5years'][i])+'_P')#genera molte regole poco significative
                      
    baskets[i].append(dfb['sales'][i])
    baskets[i].append(dfb['salary'][i])
    
baskets_lists = [b for b in baskets.values()]

#itemsets = apriori(baskets_lists, supp=2, zmin=2, target='a')

rules = apriori(baskets_lists, supp=10, zmin=2, target='r', conf=80, report='cl') 

rules = [x for x in rules if '0_P' not in x[0] and '0_P' not in x[1] and '0_W' not in x[0] and '0_W' not in x[1]] #filtro per 0 in promotion e accident
#rules = [x for x in rules if '1_L' in x[0] or '1_L' in x[1]] #filtro per chi ha lasciato
#rules = [x for x in rules if isinstance(x[0],list) and len(x[0])>1] #filtro per conseguente di lunghezza >1
#rules = [x for x in rules if 'high' in x[0] or 'high' in x[1]] #filtro per chi ha lasciato
for i in range(0,len(rules)):
	print(rules[i])
	
	
	
	
	