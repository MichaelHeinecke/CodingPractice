import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


class Difference {
    private int[] elements;
    public int maximumDifference;

    Difference(int[] elements) {
        this.elements = elements;
    }

    void computeDifference() {
        Collection<Integer> differences = new ArrayList<Integer>();

        for (int i = 0; i < elements.length; i++){
            for (int j = i + 1; j < elements.length; j++) {
                int diff = elements[i] - elements[j];
                diff = diff > 0 ? diff : -diff;
                differences.add(diff);
            }
        }

        maximumDifference = Collections.max(differences);
    }
}

class MainDifference {

    public static void main(String[] args) {
        int[] a = {1, 5, 3, 2, 9};

        Difference difference = new Difference(a);

        difference.computeDifference();

        System.out.print(difference.maximumDifference);
    }
}