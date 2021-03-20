package com.hackerrank.exercises;

import java.util.Scanner;

public class IPRegex {

    static String pattern = "\\b([0|1]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\\." +
                            "([0|1]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\\." +
                            "([0|1]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\\." +
                            "([0|1]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\\b";

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while (in.hasNext()) {
            String IP = in.next();
            System.out.println(IP.matches(pattern));
        }

    }

}
