# BOOGEYMAN
import sys, os, logging
get_file = os.path.split(os.path.abspath(__file__))
LOCAL : str = get_file[0] 
input_file : str = f"{LOCAL}/input.txt"
output_file : str = f"{LOCAL}/output.txt"
debug_file : str = f"{LOCAL}/debug.txt"
accepted_file : str = f"{LOCAL}/accepted.txt"
log_file : str = f"{LOCAL}/log.txt"


# logging.basicConfig(filename=log_file, filemode='w', format='%(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logging.basicConfig(filename=log_file, filemode='w', format='%(message)s',level=logging.INFO)

L = lambda string : logging.info(string)

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

def cmdIO() -> None:
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



# if __name__ == '__main__': launcher()





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