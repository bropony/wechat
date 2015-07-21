package rmi;

import java.util.Date;

public class Logger {
	static public void log(String ... args){
		Date dt = new Date();
		
		System.out.print("[Logger " + dt.toString() + "] ");
		for (String arg: args){
			System.out.print(arg + " ");
		}
		System.out.println();
	}
}
