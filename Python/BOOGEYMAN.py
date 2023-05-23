# BOOGEYMAN >>> Version 9.0
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

def BOOGEYMAN() -> None:
    a = si(); b = si()
    i = 0
    while i < len(a):
        if a[i] == b[-1*(i+1)]: pass
        else : break
        i+=1
    if i==len(a): print(f"YES",end="\n")
    else: print(f"NO")
    
if __name__ == "__main__":
    try: from baba_yaga import cmdIO, _generator_; cmdIO(); BOOGEYMAN(); _generator_(); 
    except (FileNotFoundError,ModuleNotFoundError): BOOGEYMAN()