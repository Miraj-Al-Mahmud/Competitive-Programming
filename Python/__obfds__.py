# obfds
import sys, os
get_file = os.path.split(os.path.abspath(__file__))
LOCAL : str = get_file[0] 
input_file : str = f"{LOCAL}/input.txt"
output_file : str = f"{LOCAL}/output.txt"
debug_file : str = f"{LOCAL}/debug.txt"
accepted_file : str = f"{LOCAL}/accepted.txt"

# moved 11-03-2023 >>> EDITED 
def debug(appendMode : str, *var) -> None:
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

def o_b_f_d_s() -> None:
	#input = lambda: sys.stdin.readline().rstrip()
	sys.stdin = open(F'{input_file}', 'r')
	sys.stdout = open(F'{output_file}', 'w')
	
def _generator_() -> None:
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


def F15() -> None: sys.stdout = open(F'{output_file}', 'w')

	







'''
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


capitalize() == toupper()
itertools.compress()
1e10
gcd lcm already in math library
iter()
most_common()

myit = iter(mytuple)
print(next(myit)) # apple

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
over_75 = list(filter(lambda x: x>75, scores)) # [90, 76, 88, 81]

>>> Those function who have the tendency to start from the left will always have a funtion that statrs with a r
count(value, startIndex, endIndex)
find(value, startIndex, endIndex)
rfind() <<< find from the left
index(value, startIndex, endIndex)
rindex() <<< index from the right
partition()
rpartition() <<< starts from the right
swapcase()
i = x.translate(dick) << for translating the order of letters
x.zfill(fillValueFromTheLeft)
try , finally keyword
# empty list, 1, 0, less than num ...    
# orderedDict -> remembers the insertionorder
# ~1 means 2 >>> apoprox value
# for i in reversed(range(0,3)): print(f"{i}",end="\n") >>> 2,1,0
# for i in range(3,-1,-1): print(i) >>> 3,2,1
# str.find()
# str.rfind()
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

# from collectuions import deque # its the full form of double ended queue
# deq = deque(listname)
# deq.appendleft(value)
# deq.popleft(value)




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


# pyrival template 
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip
# region fastio
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b: break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start: file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False): file.flush()
if sys.version_info[0] < 3: sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
else: sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
'''