# MultiLang
A multiple language tester. For weekly challenges on the TWT server.

Hey anyone using my multilang project.

So i just finished up with the java support

here's what the tester needs to do.
-Install JDK 8 or higher
-Download a package json-simple-1.1.1.jar  find it here https://code.google.com/archive/p/json-simple/downloads

-create/ edit your CLASSPATH system variable (google it) to include the package
egs:
CLASSPATH = .;c:/hello/bye/json-simple-1.1.1.jar

You're almost done. Just few more important titbits.
any solution by the user has to be in the form
'''java
public static return_type solution(some_args){
	return some_answer
}
'''

"java\n" should be the first line
the function should be public static.

If you make any changes to the 'java_temp.java' file make sure to update the variable
line_no_java in multilang.py
line_no_java should be the 1 indexed line no for the empty line between the two comments

//SOLUTION

//SOLUTION

One more important bit. in java_temp use find and replace
to replace

Some random password

with some strong random letter arrangement. It doesn't really matter as long as this doesn't get to the hands of any participant.
There are just 2 occurances of the line so you can replace manually too.
Basically a SecurityManager in java prevents any insecure action. This includes reading/writing to a file. But i have configured it to allow writing to a temporary results file (to communicate b/w multilang.py and Main) if and only if a certain static variable of the tester (Main class) is equal to the above password.

PS: I know i've used named variable for java. but we can convert it all to a dict when we need more support.
