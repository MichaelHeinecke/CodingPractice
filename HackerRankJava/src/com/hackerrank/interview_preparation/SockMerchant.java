package com.hackerrank.interview_preparation;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class SockMerchant {

    // Complete the sockMerchant function below.
    static int sockMerchant(int n, int[] ar) {
        Map<Integer, Integer> numberOfSocksPerColour = new HashMap<>();

        for (int i : ar) {
                int count = numberOfSocksPerColour.getOrDefault(i, 0);
                numberOfSocksPerColour.put(i, ++count);
        }

        int numberOfPairs = 0;

        Iterator it = numberOfSocksPerColour.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry pair = (Map.Entry) it.next();
            numberOfPairs += (int) pair.getValue() / 2;
        }

        return numberOfPairs;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        int[] sockArray = new int[] {1, 2, 3, 2, 4, 5, 1, 1};
        int numberOfPairs = sockMerchant(5, sockArray);

        System.out.println(numberOfPairs);
    }
}

