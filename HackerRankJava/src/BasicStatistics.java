import java.util.Scanner;
import java.util.Arrays;

public class BasicStatistics {

    public static int[] readArray() {
        Scanner scanner = new Scanner(System.in);
        int len = scanner.nextInt();
        scanner.nextLine();
        int[] intOutputArray = new int[len];

        for (int i = 0; i < len; i++) {
            intOutputArray[i] = scanner.nextInt();
        }

        return intOutputArray;
    }

    public static double calculateMean(int[] intArray) {
        int sum = 0;

        for (int num : intArray) {
            sum += num;
        }

        return sum / (double) intArray.length;
    }

    public static void main(String[] args) {
        int[] intArray = readArray();
        System.out.println(Arrays.toString(intArray));
        System.out.println(calculateMean(intArray));
    }
}
