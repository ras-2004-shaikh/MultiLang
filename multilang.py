import os
import time
import json

#solutions=[wherever the solutions are maybe discord?? this will be a list of strings]

test_solution='''java
public static int solution(){
	return 5;
}
'''
test_solution_2='''brainf*ck
>+++++[<++++++++++>-]<+++.
'''
solutions=[test_solution,test_solution_2]

test_file='tests.json'
temp_files={'java':'java_temp.java'}
result_files={'java':'test_fails.dat'}
temporary='Main' #this must be the name of the class in java_temp.java
remove_files={'java':[temporary+'.java',temporary+'.class',"MySecurity.class"]}
line_no_java=76

i=1
while solutions:
	sol=solutions.pop()
	print(f"Solution: {i}")
	i+=1
	sol_lines=[*map(lambda s:s+'\n',sol.split('\n'))]
	if sol_lines[0]=='java\n':
		lines=[]
		with open(temp_files['java'],'r')as f:
			lines=f.readlines()
		lines[line_no_java:line_no_java+1]=sol_lines[1:]
		with open(temporary+'.java','w')as f:
			f.writelines(lines)
		os.system(f'javac {temporary+".java"}')
		os.system(f'java {temporary} {test_file}')
		for s in remove_files['java']:
			os.remove(s)
		with open(result_files['java'],'r')as f:
			res=f.readlines()
			print(res[0])
			for line in res[1:10]:
				print(line)
		os.remove(result_files['java'])
	elif sol_lines[0]=='brainf*ck\n':
		interpreter=__import__('brainF_temp').interpret
		code=''.join(sol_lines[1:])
		with open(test_file,'r') as f:
			cases=json.load(f)['cases']
		failed_cases=[]
		start=time.time()
		for test in cases:
			try:
				ans=interpreter(code,str(test[0]))
				if(ans!=str(test[1])):
					failed_cases.append(test+["Your answer: "+ans])
			except Exception as e:
				failed_cases.append(test+["Error: "+str(e)])
		end=time.time()
		print(f"""Passed : {len(cases)-len(failed_cases)}/{len(cases)}
time: {end-start}""")
		if len(failed_cases):
			print('Some failed cases.')
			for test in failed_cases[:3]:
				print(f"""Input: {test[0]}
Actual answer: {test[1]}
{test[2]}""")



