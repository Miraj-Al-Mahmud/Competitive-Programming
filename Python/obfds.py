# obfds >>> Version 8.0
from __future__ import division, print_function
from io import BytesIO, IOBase
import os, sys, math, heapq, itertools, bisect
from string import ascii_lowercase, ascii_uppercase
from collections import deque,defaultdict, OrderedDict, Counter
ii  = lambda : int(input())                           
si  = lambda : input()                               
mi  = lambda : map(int,input().strip().split(" "))   
msi = lambda : map(str,input().strip().split(" "))   
li  = lambda : list(mi())                            
lsi = lambda : list(msi())
iseven = lambda num : num & 1 == 0 # num%2==0                       
isodd = lambda num : num & 1 == 1 # num%2==1                        
positive_infinity : float = float('inf')
negative_infinity : float = float('-inf')

def _obfds_() -> None:
    for tc in range(ii()):
        print(f"{2}",end="\n")
        
if __name__ == "__main__":
    try: from __obfds__ import o_b_f_d_s, _generator_; o_b_f_d_s(); _obfds_(); _generator_(); 
    except (FileNotFoundError,ModuleNotFoundError): _obfds_()