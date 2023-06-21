# BOOGEYMAN >>> Version 12.0
def BoogeyMan() -> None:
    '''
    Query
    '''
    n2a = {v:chr(k) for k,v in zip(range(97,97+27),range(1,27))}

    for _ in range(ii()):
        length = ii()
        s = si()
        length-=1
        sb = ""
        while length >= 0:
            if s[length]=='0':
                n = int(s[length-2]+s[length-1])
                if s[length-1]!='0':
                    sb+=n2a[n]
                    
                else:
                    if s[length-2]=='1':
                        sb+=n2a[10][::-1]
                    else:
                        sb+=n2a[20][::-1]

                length-=2
            else:
                sb+=n2a[int(s[length])]

            length-=1
        p(sb[::-1]) 

if __name__ == "__main__":
    import os, sys, math, itertools, bisect
    from collections import deque, defaultdict, OrderedDict, Counter
    # from functools import cache, lru_cache # @lru_cache(maxsize=100)
    ii,si = lambda : int(input()), lambda : input()               
    mi, msi  = lambda : map(int,input().strip().split(" ")), lambda : map(str,input().strip().split(" ")) 
    li, lsi = lambda : list(mi()), lambda : list(msi())
    out, export, p, pp = [], lambda : print('\n'.join(map(str, out))), lambda x : out.append(x), lambda array : p(' '.join(map(str,array)))
    try:
        from baba_yaga import L, cmdIO, _generator_
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
    except (FileNotFoundError,ModuleNotFoundError): input = sys.stdin.readline; BoogeyMan(); export()