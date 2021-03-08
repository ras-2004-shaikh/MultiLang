import os
import time

#solutions=[wherever the solutions are maybe discord?? this will be a list of strings]

test_solution='''java
public static int solution(){
	return 5;
}
'''
solutions=[test_solution]


java_temp='java_temp.java'
java_results='test_fails.dat'
temporary='Main' #this must be the name of the class in java_temp.java
line_no_java=76

while solutions:
	sol=solutions.pop()
	sol_lines=[*map(lambda s:s+'\n',sol.split('\n'))]
	if sol_lines[0]=='java\n':
		lines=[]
		with open(java_temp,'r')as f:
			lines=f.readlines()
		lines[line_no_java:line_no_java+1]=sol_lines[1:]
		with open(temporary+'.java','w')as f:
			f.writelines(lines)
		os.system(f'javac {temporary+".java"}')
		os.system(f'java {temporary}')
		os.remove(temporary+'.java')
		os.remove("Main.class")
		os.remove("MySecurity.class")
		with open(java_results,'r')as f:
			res=f.readlines()
			for line in res:
				print(line)
		os.remove(java_results)

