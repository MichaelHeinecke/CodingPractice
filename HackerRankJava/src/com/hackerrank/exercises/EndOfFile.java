package com.hackerrank.exercises;

import java.util.Scanner;

public class EndOfFile {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        long lineNumber = 1;

        while (sc.hasNext()) {
            String line = sc.nextLine();

            System.out.println(lineNumber++ + " " + line);
        }

    }
}