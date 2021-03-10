def interpret(code,inp,max_cell_count=30000):
	instruction_pointer=0
	cell=[0]*max_cell_count
	memory_pointer=0
	output=[]
	loop_list=[]
	while instruction_pointer<len(code):
		inst=code[instruction_pointer]
		if inst=='<':
			memory_pointer-=1
			memory_pointer%=max_cell_count
		elif inst=='>':
			memory_pointer+=1
			memory_pointer%=max_cell_count
		elif inst=='+':
			cell[memory_pointer]+=1
		elif inst=='-':
			cell[memory_pointer]-=1
		elif inst==',':
			cell[memory_pointer]=inp.pop(0)
		elif inst=='.':
			if(cell[memory_pointer]>-1):
				out=chr(cell[memory_pointer])
				output+=[out]
			else:
				raise Exception('Output for -ve pointer val not allowed.')
		elif inst=='[':
			if not cell[memory_pointer]:
				instruction_pointer=closing_loop(code,instruction_pointer)
			else: loop_list+=[instruction_pointer]
		elif inst==']':
			if cell[memory_pointer]:
				instruction_pointer=loop_list[-1]
			else: loop_list.pop()
		instruction_pointer+=1
	return ''.join(output)

def closing_loop(code,instruction_pointer):
	co=1
	for i in range(instruction_pointer+1,len(code)):
		if code[i]=='[':co+=1
		elif code[i]==']':co-=1
		if not co:
			return i
	raise Exception('Syntax error. Open loop.')
