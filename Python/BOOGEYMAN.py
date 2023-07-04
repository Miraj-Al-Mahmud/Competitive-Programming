# BOOGEYMAN >>> Version 13.0
def BoogeyMan() -> None:
    '''  Query '''
    l = [i for i in range(20)]

    class Node:
        def __init__(self,data = None): self.data,self.next,self.prev=data,None,None




    class Visualizer:
        def __init__(self, l: list):
            self.l = l
            self.idx = 1
            self.counter = 1
            self.dick = defaultdict(list)
            self.length = len(l)
            self.maxVal = max(l)

        def filler(self, num:int):
            s = str(num) if num!=0 else '00'
            return s.zfill(2)

        def adder(self):
            self.dick[0].append(self.l[0]) # add the first element
            while self.idx < self.length:
                try:
                    start = (2**self.idx)-1
                    end = (2**(self.idx+1))-1
                    for i in range(start,end): self.dick[self.counter].append(self.filler(self.l[i]))
                    self.counter+=1
                    self.idx += 1
                except IndexError: break

        def height_shortener(self, height) -> list:
            store = [0,2]
            counter = idx = 2
            while counter < height:
                idx = idx*2 + 1
                store.append(idx)
                counter+=1
            return store

        def printer(self):
            h = self.height_shortener(self.counter+1)
            idx = -1
            for k,v in self.dick.items():
                print(f"{' '*h[idx]}",end="") # before space for nums
                for nums in v: print(f"{nums}{' '*(h[idx+1]-1)}",end="") # the elements
                print(f"",end="\n")
                idx-=1

                """
                try:
                    print(f"{' '*(h[idx]+2)}",end="") # space before the tree branch >>> added 2 instead of -1
                    nodes = len(v)
                    #for nums in range(nodes-1): print(f"{'-'*(h[idx+1]-1)}{' '*(h[idx+1]-1)}",end="") # the branches
                    for nums in range(nodes): print(f"{'-'*(h[idx+1]-1)}{' '*(h[idx+1]+2)}",end="") # the branches
                    print(f"",end="\n")
                except IndexError: pass
                """
            L(h)



        def process(self):
            self.adder()
            self.printer()

    v = Visualizer(l)
    v.process()



    def insertLevelOrder(arr, i, n):
        root = None
        if i < n:
            root = Node(arr[i])
            # first add all left the all right
            root.left = insertLevelOrder(arr, 2 * i + 1, n)
            root.right = insertLevelOrder(arr, 2 * i + 2, n)
        return root

    inorderStore = []
    def inorder(root):
        # In - Order >>> Left - Process - Right
        if root: inorder(root.left); inorderStore.append(root.data); inorder(root.right)
        return inorderStore


            
if __name__ == "__main__":
    import os, sys, math, itertools, bisect
    from collections import deque, defaultdict, OrderedDict, Counter
    # from functools import cache, lru_cache # @lru_cache(maxsize=100)
    ii,si = lambda : int(input()), lambda : input()               
    mi, msi  = lambda : map(int,input().strip().split(" ")), lambda : map(str,input().strip().split(" ")) 
    li, lsi = lambda : list(mi()), lambda : list(msi())
    out, export, p, pp = [], lambda : print('\n'.join(map(str, out))), lambda x : out.append(x), lambda array : p(' '.join(map(str,array)))
    try:
        from baba_yaga import L, LT, cmdIO, _generator_
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