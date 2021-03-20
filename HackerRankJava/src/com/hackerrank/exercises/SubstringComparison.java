package com.hackerrank.exercises;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class SubstringComparison {

    public static String getSmallestAndLargest(String s, int k) {
        // smallest and largest string by lexicographical order
        String smallest = "";
        String largest = "";
        List<String> substrings = new ArrayList<>();

        // create list of substrings
        for (int i = 0; i <= s.length() - k; i++) {
            String substring = s.substring(i, i + k);
            substrings.add(substring);
        }

        // sort lexicographically
        List<String> sortedSubstrings = substrings
                .stream()
                .sorted(String::compareTo)
                .collect(Collectors.toList());

        smallest = sortedSubstrings.get(0);
        largest = sortedSubstrings.get(sortedSubstrings.size() - 1);

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
