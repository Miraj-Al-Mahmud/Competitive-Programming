# BOOGEYMAN >>> Version 11.0
import os, sys, math, itertools, bisect
from string import ascii_lowercase, ascii_uppercase
from collections import deque, defaultdict, OrderedDict, Counter
ii,si = lambda : int(input()), lambda : input()               
mi, msi  = lambda : map(int,input().strip().split(" ")), lambda : map(str,input().strip().split(" ")) 
li, lsi = lambda : list(mi()), lambda : list(msi())

def BoogeyMan() -> None:
    '''
    Query
    '''
    for tc in range(ii()):
        length = ii()
        s = si()
        store = []
        prev = s[0]
        idx = 1
        while idx < length:
            try:
                if s[idx] == prev:
                    store.append(s[idx])
                    prev = s[idx+1]
                    idx+=2
                else: idx+=1
            except IndexError: break
        print(f"{''.join(store)}",end="\n")
        
            
    
    
        
if __name__ == "__main__":
    try:
        from baba_yaga import cmdIO, _generator_
        class _BoogeyMan_:
            def __init__(self) -> None: self.launchers = [cmdIO(), BoogeyMan(), _generator_()]
            def init(self) -> None:
                for _ in self.launchers: yield _ ; assert not _ , "EOF" 
        _BoogeyMan_().init()
    except (FileNotFoundError,ModuleNotFoundError): BoogeyMan()