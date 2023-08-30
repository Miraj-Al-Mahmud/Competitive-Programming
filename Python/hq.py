# BOOGEYMAN
import sys, os, logging, math
from collections import defaultdict, Counter
get_file = os.path.split(os.path.abspath(__file__))
LOCAL : str = get_file[0] 
input_file : str = f"{LOCAL}/input.txt"
output_file : str = f"{LOCAL}/output.txt"
debug_file : str = f"{LOCAL}/debug.txt"
accepted_file : str = f"{LOCAL}/accepted.txt"
log_file : str = f"{LOCAL}/log.txt"

# logging.basicConfig(filename=log_file, filemode='w', format='%(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logging.basicConfig(filename=log_file, filemode='w', format='%(message)s',level=logging.INFO) #logging defaults

L = lambda string : logging.info(string) # basic log as string
def LT(tc, custom, string) : # custo log with matching testcase
	tc+=1
	if tc == custom: logging.info(string)

# moved 11-03-2023 >>> EDITED 
def debug(appendMode : str, *var) -> None: # deprecated !!! >>> substituted by log module
	if appendMode == "a":
		with open(debug_file, 'r') as f:
			lines = f.readlines()
			counter = 0
			for line in lines:
				if line.startswith("Query"): counter += 1
		with open(debug_file, 'a') as f:
			for idx,v in enumerate(var, start=counter): f.write(f"Query {idx+1}\t>-> {str(v)}\n") 
	else:
		with open(debug_file, 'w') as f:
			for idx,v in enumerate(var): f.write(f"Query {idx+1}\t>-> {str(v)}\n")

def cmdIO() -> None: # standard input output for python commands instead of terminus package
	#input = lambda: sys.stdin.readline().rstrip()
	sys.stdin = open(F'{input_file}', 'r')
	sys.stdout = open(F'{output_file}', 'w')
	
def GEN() -> None: # to match the generated result with the AC output as testcases only for native use
	# close the previous file first, otherwise it won't work
	sys.stdout.close()
	with open(output_file, 'r+') as f: generated = f.readlines()
	# lines is the main list to compare to
	with open(accepted_file, 'r+') as g: fromCodeforces = g.readlines()
	# the testcases provided from Codeforces
	# level up the new line
	try:
		if generated[-1].endswith('\n') and len(generated)!=0 and len(fromCodeforces)!=0: fromCodeforces[-1]+='\n'
		flag = False
		lengthOfGenerated = len(generated)
		lengthOfCodeforces = len(fromCodeforces)
		errorCollector = []
		# if the length is same
		if len(generated)==len(fromCodeforces) :
			for idx,i,j in zip(range(1,len(generated)+1), generated, fromCodeforces):
				# found - expected
				if i!=j : flag = True; errorCollector.append(idx); errorCollector.append(i); errorCollector.append(j); break
			if flag == False :
				# Means success !!!
				with open(output_file, 'w') as h:
					h.write(f"Verdict	>->\t\tOK\n")
					h.write(f"A/C		>->\t\t{lengthOfGenerated}/{lengthOfCodeforces}")
			elif flag == True :
				with open(output_file, 'w') as h:
					h.write(f"Verdict		>->\t\tWrong Answer\n")
					h.write(f"A/C			>->\t\tError at line {errorCollector[0]}/{lengthOfGenerated}\n")
					h.write(f"Expected 	>->\t\t'{errorCollector[2].rstrip()}'\n")
					h.write(f"Got 	 	>->\t\t'{errorCollector[1].rstrip()}'")
	# new addition 26/11/2022
	except IndexError : pass


def F15() -> None: sys.stdout = open(F'{output_file}', 'w') # deprecated


class Visualizer: # A graph visualizer for list to graph conversion
    def __init__(self, l: list):
        self.l = l
        self.idx = 1
        self.counter = 1
        self.store = []
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
            # print(f"{' '*h[idx]}",end="") # before space for nums
            temp = []
            temp.append(f"{' '*h[idx]}")
            #for nums in v: print(f"{nums}{' '*(h[idx+1]-1)}",end="") # the elements
            for nums in v: temp.append(f"{nums}{' '*(h[idx+1]-1)}")
            #temp.append('\n')
            idx-=1
            self.store.append(''.join(temp))

            """ Code for adding the hyphens
            try:
                print(f"{' '*(h[idx]+2)}",end="") # space before the tree branch >>> added 2 instead of -1
                nodes = len(v)
                #for nums in range(nodes-1): print(f"{'-'*(h[idx+1]-1)}{' '*(h[idx+1]-1)}",end="") # the branches
                for nums in range(nodes): print(f"{'-'*(h[idx+1]-1)}{' '*(h[idx+1]+2)}",end="") # the branches
                print(f"",end="\n")
            except IndexError: pass
            """
        return self.store

    def process(self) -> list:
        self.adder()
        self.printer()
        return self.store

def see(l:list): # Aid of Visualizer class
    v = Visualizer(l)
    temp = v.process()
    for i in temp: L(i)

class INFO: # Displays info about a specific array
    def __init__(self, l : list):
        self.l = l
        self.len = len(l)
        self.sorted_list = sorted(self.l)
        self.reversed_sorted = self.sorted_list[::-1]
        self.counter = Counter(self.l)
        self.display = []
    
    def isPrime( self, n : int ) -> bool:
        if n <= 1: return False
        if n % 2 == 0: return n == 2
        max_div = math.floor(math.sqrt(n))
        for i in range(3, 1 + max_div, 2):
            if n % i == 0: return False
        return True

    def all_primes(self) -> list: return [i for i in self.l if self.isPrime(i)]


    def numerical(self) -> None:
        s = self.display.append
        nl = lambda : s('\n')
        s('Regular\t\t>->\t'); s(self.l); nl()
        # sorted
        s('Sorted\t\t>->\t'); s(self.sorted_list); nl()
        # reversed
        s('Reverse\t\t>->\t'); s(self.reversed_sorted); nl()
        # counter
        s('Counter\t\t>->\t')
        tempStore = []
        for k,v in self.counter.items():
        	tempStore.append(f"{k},{v}")
        s(" | ".join(map(str,tempStore)))
        nl()
        # set
        s('Set\t\t\t>->\t'); s(set(self.l)); nl();
        # primes
        kk = self.all_primes()
        s("Primes\t\t>->\t"); s(f"{len(kk)} >-> "); s(kk); nl()
        # evens
        ev = [i for i in self.l if i%2==0]
        s("Evens\t\t>->\t"); s(f"{len(ev)} >-> "); s(ev); nl()
        # odds
        od = [i for i in self.l if i%2==1]
        s("Odds\t\t>->\t"); s(f"{len(od)} >-> "); s(od); nl()
        # unique nums
        un = [k for k,v in self.counter.items() if v == 1]
        s('Unique\t\t>->\t'); s(f'{len(un)} >-> '); s(un); nl()
        # dups
        dups = [k for k,v in self.counter.items() if v > 1]
        s('Dups\t\t>->\t'); s(f'{len(dups)} >-> '); s(dups); nl()


        L("".join(map(str,self.display)))

    def alphabetical(self):
        s = self.display.append
        nl = lambda : s('\n')
        # Given list
        s('Regular\t\t>->\t'); s(self.l); nl()
        # sorted
        s('Sorted lex\t>->\t'); s(self.sorted_list); nl()
        # sorted len
        s('Sorted len\t>->\t'); s(sorted(self.l, key=len)); nl()
        # reversed
        s('Reverse\t\t>->\t'); s(self.sorted_list); nl()
        # counter
        s('Counter\t\t>->\t')
        tempStore = []
        for k,v in self.counter.items():
            tempStore.append(f"{k},{v}")
        s(" | ".join(map(str,tempStore)))
        nl()
        # unique
        un = [k for k,v in self.counter.items() if v == 1]
        s('Unique\t\t>->\t'); s(f'{len(un)} >-> '); s(un); nl()
        # dups
        dups = [k for k,v in self.counter.items() if v > 1]
        s('Dups\t\t>->\t'); s(f'{len(dups)} >-> '); s(dups); nl()



        L("".join(map(str,self.display)))

    def processor(self): self.numerical() if str(self.l[0]).isnumeric() else self.alphabetical()

def info( l : list): i = INFO(l); i.processor()





# if __name__ == '__main__': launcher()





'''


locals()
globals()
dir() >>> name of all variables

Color Scheme
Monokai Markdown
Oceanic Next Markdown
Sixteen

# hisort
# rhoist
# iamrj
# ajmir
# awesome
# emosewa
# a-w-e-s-o-m-e
# A-W-E-S-O-M-E
# AwEsOmE



filter(lambda x: something, array_name)
itertools.product(array1, array2) >>> basically makes pair

def dec(function):
    def wrapper():
        print(f"My name is Miraj Al Mahmud Khan",end="\n")
        function()
    return wrapper
    
itertools.dropwhile(lambda x:)
itertools.takewhile(lambda x:)
itertools.compress(first_array, second_array) like the zip function returns the bool
most_common()


scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
over_75 = list(filter(lambda x: x>75, scores)) # [90, 76, 88, 81]

>>> Those function who have the tendency to start from the left will always have a funtion that statrs with a r
arrayname.count(value)
index(value, startIndex, endIndex)
rindex() <<< index from the right

partition() >>> makes 3 values from a string
rpartition() <<< starts from the right

swapcase()

string.zfill(num_to_fill) >>> for printing
try , finally keyword


# ~1 means 2 >>> apoprox value
# for i in reversed(range(0,3)): print(f"{i}",end="\n") >>> 2,1,0
# for i in range(3,-1,-1): print(i) >>> 3,2,1

# str.endswith("is", 2, 4)

# cars.sort(key=lambda x: len(x) )
# for else

# bisect.bisect_left returns the leftmost place in the sorted list to insert the given element
# bisect.bisect_right returns the rightmost place in the sorted list to insert the given element

# divmod(8,3) >>> (2,2)

not necessary to put the start and end points in an array
# def gen() : yield 1; yield 2; yield 3
# x = gen()
# print(f"{next(x)}",end="\n")
# print(f"{next(x)}",end="\n")






Competitive Programming Topics >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

XOR >>> If two >>> 0, If one >>> 1
1 ^ 1 = 0
0 ^ 0 = 1
0 ^ 1 = 1
1 ^ 0 = 1


left shift << multiplying with the power of 2
right shift >> dividing with the power of 2

x & 1 = if 0 then the number is even and if 1 then the number is odd
i.e. 3 & 1 = 1, 2 & 1 = 0

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# backed up for future use

'''