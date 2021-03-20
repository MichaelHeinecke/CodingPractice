package encryptdecrypt;

import java.util.Arrays;

public class Main {

    private static String encrypt(String stringToEncrypt) {

//        char[] charArrayToEncrypt = stringToEncrypt.toCharArray();
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        String reversedAlphabet = "zyxwvutsrqponmlkjihgfedcba";

        String encryptedString = stringToEncrypt.chars()
                .mapToObj(i -> (char) i)
                .map(c -> alphabet.indexOf(c) == -1 ? c : alphabet.indexOf(c))
                .map(i -> reversedAlphabet.charAt(i) == -1 ? i : reversedAlphabet.charAt(i))
                .collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append)
                .toString();

        return encryptedString;
    }

    public static void main(String[] args) {
        String string = "we found a treasure!";
        System.out.println(string);

        String encryptedString = encrypt("we found a treasure!");
        System.out.println(encryptedString);
    }
}
