


import os,sys,hq,math,itertools;from collections import deque,defaultdict,OrderedDict,Counter
from bisect import bisect,bisect_left,bisect_right,insort
from heapq import heapify,heappush,heappop,nsmallest,nlargest,heapreplace, heappushpop
sys.stdin = open(F'{hq.input_file}','r')
sys.stdout = open(F'{hq.output_file}', 'w')



import psutil
import datetime

def formatter():
    # returns the time in seconds since the epoch
    last_reboot = psutil.boot_time()
     
    # converting the date and time in readable format
    result = datetime.datetime.fromtimestamp(last_reboot)
    one = str(result).split()
    tarikh = ''.join(one[0].split('-'))
    somoy = "".join((one[1].split('.')[0]).split(':'))
    final = f'{somoy}_{tarikh}'
    print(f"{final}",end="\n")

formatter()

