# BOOGEYMAN >>> Version 13.0
def BoogeyMan() -> None:
    '''  Query '''
    l = [1,2,4,5,6,4,3,2,1]
    info(l)
            
if __name__ == "__main__":
    import os, sys, math, itertools, bisect
    from collections import deque, defaultdict, OrderedDict, Counter
    # from functools import cache, lru_cache # @lru_cache(maxsize=100)
    ii,si = lambda : int(input()), lambda : input()               
    mi, msi  = lambda : map(int,input().strip().split(" ")), lambda : map(str,input().strip().split(" ")) 
    li, lsi = lambda : list(mi()), lambda : list(msi())
    out, export, p, pp = [], lambda : print('\n'.join(map(str, out))), lambda x : out.append(x), lambda array : p(' '.join(map(str,array)))
    try:
        from baba_yaga import L, LT, see, info, cmdIO, _generator_
        class _BoogeyMan_:
            def __init__(self) -> None: self.launchers = [cmdIO(), BoogeyMan(), export(), _generator_()]
            def init(self) -> None:
                for _ in self.launchers: yield _ ; assert not _ , "EOF" 
            def container(fun) :
                def wrapper(): print(f"Success",end="\n"); fun()
                return wrapper
        @_BoogeyMan_.container
        def assembler() : _BoogeyMan_().init()
        assembler()
    except (FileNotFoundError,ModuleNotFoundError): BoogeyMan(); export()