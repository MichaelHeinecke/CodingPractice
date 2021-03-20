package com.hackerrank.exercises;

import java.util.Scanner;

public class StringTokens {

    static String[] tokenize(String s) {
        String[] array = s.split("[^a-zA-Z]+");
        return array;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        scan.close();

        s = s.trim();

        if (s.length() > 0) {
            String[] tokenArray = tokenize(s);

            System.out.println(tokenArray.length);
            for (String token : tokenArray) {
                System.out.println(token);
            }
        } else {
            System.out.println(0);
        }
    }
}

