import java.util.Scanner;

class Main {

    static String[] reverseArray(String[] stringArray) {
        for (int i = 0; i < stringArray.length / 2; i++) {
            String temp = stringArray[i];
            stringArray[i] = stringArray[stringArray.length - 1 - i];
            stringArray[stringArray.length - 1 - i] = temp;
        }

        return stringArray;
    }


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] strings = new String[3];

        for (int i = 0; i < 3; i++) {
            strings[i] = scanner.next();
        }

        strings = reverseArray(strings);

        for (String str : strings) {
            System.out.println(str);
        }

    }
}