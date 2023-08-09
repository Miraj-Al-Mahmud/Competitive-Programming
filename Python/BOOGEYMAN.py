# Version 17.0
def main() -> None:
    # 2023-08-09 23:31:38
    for tc in range(ii()):
        length = ii()
        print('YNEOS'[sum(li())%2==0::2])



            
if __name__ == "__main__":
    master_flag = False
    L = lambda string: exec('from hq import L\nL(string)') if not master_flag else False
    LT = lambda tc, custom, string: exec('from hq import LT\nLT(tc, custom, string)') if not master_flag else False
    import os,sys,math,itertools;from collections import deque,defaultdict,OrderedDict,Counter
    from bisect import bisect,bisect_left,bisect_right,insort
    from heapq import heapify,heappush,heappop,nsmallest,nlargest,heapreplace, heappushpop
    ii,si=lambda:int(input()),lambda:input()               
    mi,msi=lambda:map(int,input().strip().split(" ")),lambda:map(str,input().strip().split(" ")) 
    li,lsi=lambda:list(mi()),lambda:list(msi())
    out,export,p,pp=[],lambda:print('\n'.join(map(str, out))),lambda x :out.append(x),lambda array:p(' '.join(map(str,array)))
    try:exec('from hq import see,info,cmdIO,_generator_\nline=[cmdIO(),main(),export(),_generator_()]\nfor l in line:l')
    except(FileNotFoundError,ModuleNotFoundError):master_flag=True;main();export()