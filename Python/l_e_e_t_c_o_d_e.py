# @copyright BOOGEYMAN
# LEETCODE simplifier V3




def main() -> None:
	
	
	


	sequence = "ababc"
	word = "ab"


	length = len(word)
	c = 0
	for idx,s in enumerate(sequence):
		try:
			ans = sequence.index(word, idx,idx+length-1)
			c+=1
		except ValueError: pass
	return c


	


	
		
	
	
			
			
		
		



if __name__ == '__main__':
	import baba_yaga
	from baba_yaga import L
	
	raincheck = main()
	if raincheck == False: print(f"false",end="\n")
	elif raincheck == True: print(f"true",end="\n")
	elif raincheck==None: print(f"<-< No value to return >->",end="\n")
	else: print(f'{raincheck}',end="\n")
	
	baba_yaga._generator_()







