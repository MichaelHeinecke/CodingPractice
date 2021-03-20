package com.hackerrank.exercises;

import java.util.Scanner;

public class PalindromeCheck {

        public static void main(String[] args) {

            Scanner sc=new Scanner(System.in);
            String A=sc.next();

            StringBuilder sb = new StringBuilder();

            sb.append(A);
            String reversedString = sb.reverse().toString();

            System.out.println(A.equals(reversedString) ? "Yes" : "No");

        }
}
