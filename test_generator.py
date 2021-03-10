import random, json
from tqdm import tqdm
#solution if required(also any other user defined functions)
solution = lambda *args: "hello world"



#solution if required(also any other user defined functions)

#generator for test cases.
#All test cases of form (*args , output)

# arguments for generator.
# Eg: maximum / minimum for some random variable
# compulsory arguments

test_count=1000 # No of test cases
test_cases_file="tests.json" # json file for test cases.


#IMPORTANT
def test_generator():
	pass
	#remove the pass and create a generator to yield the test cases. For example:
	for _ in range(test_count):
		test=[(),5]
		yield test

cases = [*test_generator()]  
#IMPORTANT


with open(test_cases_file,"w")as f:
	json.dump({"cases":cases},f)