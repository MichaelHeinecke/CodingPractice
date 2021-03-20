package com.hackerrank.exercises;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Scanner;

public class CountNumbersInFile {
    public static void main(String[] args) {
        System.out.println(countEvenNumbersInFile());
    }

    private static int countEvenNumbersInFile() {
        int counter = 0;
        try (Scanner sc = new Scanner(new FileReader("./HackerRankJava/resources/dataset_91065.txt"))) {
            while (sc.hasNext()) {
                int number = sc.nextInt();

                if (number == 0) {
                    break;
                } else if (number % 2 == 0) {
                    counter++;
                }

            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        return counter;
    }

}
