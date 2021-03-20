package com.hackerrank.exercises;

import java.util.Scanner;

public class Loops2 {
	
	private static int recursiveSum(int b, int n) {

		if (n == 0) {
			return b;
		} else {
			// 1 <= n <= 15
			return (int) Math.pow(2, n) * b + recursiveSum(b, --n);
		}
	}
	
	public static void main(String []args){
	    Scanner in = new Scanner(System.in);
	    int t = in.nextInt();
	    for(int i=0; i<t; i++){
	        int a = in.nextInt();
	        int b = in.nextInt();
	        int n = in.nextInt();
	        
	        String resultToPrint = "";
	        for (int j = 0; j < n; j++) {
	        	resultToPrint += Integer.toString(a + recursiveSum(b, j));
	        	
	        	if (j != n) {
	        		resultToPrint += " ";
	        	}
	        }
	        
	        System.out.println(resultToPrint);
	    }
	    in.close();
	}

}
