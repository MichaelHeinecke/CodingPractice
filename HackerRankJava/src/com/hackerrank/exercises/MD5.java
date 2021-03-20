package com.hackerrank.exercises;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

public class MD5 {

    private static String bytesToHex(byte[] bytes) {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < bytes.length; i++) {
            sb.append(Character.forDigit((bytes[i] >> 4) & 0xF, 16));
            sb.append(Character.forDigit((bytes[i] & 0xF), 16));
        }

        return sb.toString();
    }

    private static String encode(String string) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] hash = md.digest(string.getBytes());
        String encodedString = bytesToHex(hash);
        
        return encodedString;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String string = sc.next();

        String hash = "";

        try {
            hash = encode(string);
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }

        System.out.println(hash);
    }

}
