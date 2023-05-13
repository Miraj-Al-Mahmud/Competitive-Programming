# @copyright m-a-v-e-r-i-c-k
# LEETCODE simplifier V2

def debug(appendMode, *var) -> None:
    import t_o_p_g_u_n
    with open(t_o_p_g_u_n.debug_file,appendMode) as f:
        for idx,v in enumerate(var): f.write(f"Query {idx+1}\t>-> {str(v)}\n")


def m_a_v_e_r_i_c_k() -> None:
	pass
	


if __name__ == '__main__':
	import t_o_p_g_u_n
	t_o_p_g_u_n.F15()
	raincheck = m_a_v_e_r_i_c_k()
	if raincheck == False: print(f"false",end="\n")
	elif raincheck == True: print(f"true",end="\n")
	elif raincheck==None: print(f"<-< No value to return >->",end="\n")
	else: print(f'{raincheck}',end="\n")
	
	t_o_p_g_u_n._generator_()







