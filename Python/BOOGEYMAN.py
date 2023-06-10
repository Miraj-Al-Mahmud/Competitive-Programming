# BOOGEYMAN >>> Version 12.0
def BoogeyMan() -> None:
    '''
    Query
    '''
    Query
            
if __name__ == "__main__":
    import os, sys, math, itertools, bisect
    from collections import deque, defaultdict, OrderedDict, Counter
    from functools import cache, lru_cache # @lru_cache(maxsize=100)
    ii,si = lambda : int(input()), lambda : input()               
    mi, msi  = lambda : map(int,input().strip().split(" ")), lambda : map(str,input().strip().split(" ")) 
    li, lsi = lambda : list(mi()), lambda : list(msi())
    try:
        from baba_yaga import cmdIO, _generator_, logging, log as L
        class _BoogeyMan_:
            def __init__(self) -> None: self.launchers = [cmdIO(), BoogeyMan(), _generator_()]
            def init(self) -> None:
                for _ in self.launchers: yield _ ; assert not _ , "EOF" 
            def container(fun) :
                def wrapper(): print(f"AC",end="\n"); fun()
                return wrapper
        @_BoogeyMan_.container
        def launcher() : _BoogeyMan_().init()
        launcher()
    except (FileNotFoundError,ModuleNotFoundError): BoogeyMan()