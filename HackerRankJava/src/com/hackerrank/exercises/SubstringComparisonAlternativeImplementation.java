package com.hackerrank.exercises;

import java.util.Scanner;

public class SubstringComparisonAlternativeImplementation {

    public static String getSmallestAndLargest(String s, int k) {
        // smallest and largest string by lexicographical order
        String smallest = "";
        String largest = "";
        java.util.SortedSet<String> substringSet = new java.util.TreeSet<>();

        // create sorted set of substrings
        for (int i = 0; i <= s.length() - k; i++) {
            String substring = s.substring(i, i + k);
            substringSet.add(substring);
        }

        smallest = substringSet.first();
        largest = substringSet.last();

        return smallest + "\n" + largest;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();

        System.out.println(getSmallestAndLargest(s, k));
    }
}
