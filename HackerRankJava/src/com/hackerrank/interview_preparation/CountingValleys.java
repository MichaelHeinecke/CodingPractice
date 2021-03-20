package com.hackerrank.interview_preparation;

import java.io.IOException;
import java.util.Scanner;

public class CountingValleys {

    private static final Scanner scanner = new Scanner(System.in);

    // Complete the countingValleys function below.
    static int countingValleys(int n, String s) {
        String[] stepLetters = s.split("");

        int altitude = 0;
        int valleyCount = 0;

        for (String step : stepLetters) {

            if (step.equals("D")) {
                altitude--;
            } else if (step.equals("U") && altitude == -1) {
                valleyCount++;
                altitude++;
            } else if (step.equals("U")) {
                altitude++;
            }
        }

        return valleyCount;
    }

    public static void main(String[] args) throws IOException {
        int n = 8;
        String s = "UDDDUDUUDU";

        int result = countingValleys(n, s);

        System.out.println(result);
    }
}
