# @copyright m-a-v-e-r-i-c-k
# LEETCODE simplifier V2

def debug(appendMode, *var) -> None:
    import t_o_p_g_u_n
    with open(t_o_p_g_u_n.debug_file,appendMode) as f:
        for idx,v in enumerate(var): f.write(f"Query {idx+1}\t>-> {str(v)}\n")


def m_a_v_e_r_i_c_k() -> None:
	words = ["are","amy","u"]
	left = 0
	right = 2
	vowels = ['a','e','i','o','u']
	counter = 0
	for idx,w in enumerate(words):
	    if idx >= left and idx <= right:
	        if w[0] in vowels and w[-1] in vowels: counter+=1
	return counter



if __name__ == '__main__':
	import __obfds__
	__obfds__.F15()
	raincheck = m_a_v_e_r_i_c_k()
	if raincheck == False: print(f"false",end="\n")
	elif raincheck == True: print(f"true",end="\n")
	elif raincheck==None: print(f"<-< No value to return >->",end="\n")
	else: print(f'{raincheck}',end="\n")
	
	__obfds__._generator_()







