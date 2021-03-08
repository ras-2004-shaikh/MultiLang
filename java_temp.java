import java.util.*;
import java.io.*;
import java.lang.reflect.*;
import org.json.simple.*;
import org.json.simple.parser.*;

class MySecurity extends SecurityManager{
	public MySecurity(){
		super();
	}
	public void checkWrite(String file){
		if(file!=Main.RES_FILE || !Main.pass.equals("Some random password")){
			throw new SecurityException("Aha trying to mess. With my file system?? You fail Muhahaha.");
		}
	}
}

public class Main{
	public static final String RES_FILE="test_fails.dat";
	public static String pass="not the random password";

	public static void main(String[] args)throws Exception
	{
		Scanner sc=new Scanner(new File("tests.json"));
		String s=sc.nextLine();
		JSONParser parser=new JSONParser();
		Object obj=parser.parse(s);
		JSONObject data=(JSONObject)obj;
		JSONArray tests=(JSONArray)data.get("cases");
		List<List<Object>> failed_cases=new ArrayList<List<Object>>();
		System.setSecurityManager(new MySecurity());
		for(Object tst:tests){
			JSONArray test=(JSONArray)tst;
			List<Object> objs=new ArrayList<Object>();
			for(Object arg:test.subList(0,test.size()-1)){
				objs.add(arg);
			}
			Class main=Class.forName("Main");
			Method[] meths=main.getMethods();
			Method solution=null;
			for(Method meth:meths){
				if(meth.getName().equals("solution"))solution=meth;
			}
			if(solution==null){
				System.out.println("No public solution");
			}
			Object ans=null;
			try{
				ans=solution.invoke(null,objs.toArray());
			}
			catch(Exception e){
				List<Object> failed=new ArrayList<Object>();
				for(Object t:test)failed.add(t);
				failed.add("Error: "+e.toString());
				failed_cases.add(failed);
			}
			if(ans!=null && !ans.toString().equals(test.get(test.size()-1).toString())){
				List<Object> failed=new ArrayList<Object>();
				for(Object t:test)failed.add(t);
				failed.add("Your Answer: "+ans.toString());
				failed_cases.add(failed);
			}
		}
		pass="Some random password";
		PrintStream ps=new PrintStream(RES_FILE);
		for(List<Object> test:failed_cases){
			ps.println("Test: ");
			ps.println(test.subList(0,test.size()-1).toString());
			ps.println("Actual answer: ");
			ps.println(test.get(test.size()-2).toString());
			ps.println(test.get(test.size()-1).toString());
		}
		pass="not the random password";
	}
	//SOLUTION
	
	//SOLUTION
}
