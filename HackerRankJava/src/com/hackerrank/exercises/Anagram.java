package com.hackerrank.exercises;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Anagram {

    static boolean isAnagram(String a, String b) {
        String lowerA = a.toLowerCase();
        String lowerB = b.toLowerCase();

        Map<Character, Integer> letterFrequencyA = getLetterFrequency(lowerA);
        Map<Character, Integer> letterFrequencyB = getLetterFrequency(lowerB);

        return letterFrequencyA.equals(letterFrequencyB);
    }

    static Map<Character, Integer> getLetterFrequency(String word) {
        Map<Character, Integer> letterFrequency = new HashMap<>();

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            letterFrequency.put(c, letterFrequency.getOrDefault(c, 0) + 1);
        }

        return letterFrequency;
    }

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}

