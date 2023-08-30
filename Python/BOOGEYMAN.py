# Version 18.0
def main() -> None:
    # 2023-08-30 23:55:07
    L(1)            
if __name__ == "__main__":
    import os, sys, math, itertools
    from collections import deque, defaultdict, OrderedDict, Counter
    from bisect import bisect, bisect_left, bisect_right, insort
    from heapq import heapify, heappush, heappop, nsmallest, nlargest, heapreplace, heappushpop
    ii, si = lambda : int(input()), lambda:input()               
    mi, msi = lambda : map(int,input().strip().split(" ")), lambda:map(str,input().strip().split(" ")) 
    li,lsi = lambda:list(mi()), lambda:list(msi())
    out, export = [], lambda:print('\n'.join(map(str, out)), end='')
    p, pp = lambda x : out.append(x), lambda array : p(' '.join(map(str,array)))
    try :
        from hq import *
        patcher()
    except ( FileNotFoundError, ModuleNotFoundError ) : main(); export()


