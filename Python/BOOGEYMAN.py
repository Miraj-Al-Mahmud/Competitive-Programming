# main >>> Version 16.0
def main() -> None:
    L(1)
            
if __name__ == "__main__":
    import os, sys, math, itertools, bisect; from collections import deque, defaultdict, OrderedDict, Counter
    ii,si = lambda : int(input()), lambda : input()               
    mi, msi  = lambda : map(int,input().strip().split(" ")), lambda : map(str,input().strip().split(" ")) 
    li, lsi = lambda : list(mi()), lambda : list(msi())
    out, export, p, pp = [], lambda : print('\n'.join(map(str, out))), lambda x : out.append(x), lambda array : p(' '.join(map(str,array)))
    try: exec('from hq import L, LT, see, info, cmdIO, _generator_ \nline = [cmdIO(), main(), export(), _generator_()] \nfor l in line: l')
    except (FileNotFoundError,ModuleNotFoundError): main(); export()