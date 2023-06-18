# BOOGEYMAN >>> Version 12.0
def BoogeyMan() -> None:
    '''
    Query
    '''
    for _ in range(ii()):
        length = ii()
        s = si()
        c = len(s)
        start = 0
        end = len(s)-1
        try:
            if len(s)==1: c = 1
            else:
                while True:
                    if s[start] == s[end]: break
                    else:
                        start+=1
                        end-=1
                        c-=2
        except IndexError: c = 0
        print(f"{c}",end="\n")
            
if __name__ == "__main__":
    import os, sys, math, itertools, bisect
    from collections import deque, defaultdict, OrderedDict, Counter
    # from functools import cache, lru_cache # @lru_cache(maxsize=100)
    ii,si = lambda : int(input()), lambda : input()               
    mi, msi  = lambda : map(int,input().strip().split(" ")), lambda : map(str,input().strip().split(" ")) 
    li, lsi = lambda : list(mi()), lambda : list(msi())
    try:
        from baba_yaga import L, cmdIO, _generator_
        class _BoogeyMan_:
            def __init__(self) -> None: self.launchers = [cmdIO(), BoogeyMan(), _generator_()]
            def init(self) -> None:
                for _ in self.launchers: yield _ ; assert not _ , "EOF" 
            def container(fun) :
                def wrapper(): print(f"Success",end="\n"); fun()
                return wrapper
        @_BoogeyMan_.container
        def assembler() : _BoogeyMan_().init()
        assembler()
    except (FileNotFoundError,ModuleNotFoundError): BoogeyMan()