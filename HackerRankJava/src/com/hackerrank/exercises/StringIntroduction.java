package com.hackerrank.exercises;

import java.util.Scanner;

public class StringIntroduction {
    public static String capitalise(String word) {
        String firstLetter = word.substring(0, 1).toUpperCase();
        String restOfWord = word.substring(1);

        return firstLetter + restOfWord;
    }

    public static String compare(String a, String b) {
        return a.compareTo(b) > 0 ? "Yes" : "No";
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        String B = sc.next();

        System.out.println(A.length() + B.length());
        System.out.println(compare(A, B));
        System.out.println(capitalise(A) + " " + capitalise(B));

    }
}
