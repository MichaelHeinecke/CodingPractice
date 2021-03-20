import java.util.Arrays;

public class JadenCase {

    public static String capitalize(String word) {
        return word.substring(0, 1).toUpperCase() + word.substring(1).toLowerCase();
    }

    public String toJadenCase(String phrase) {

        if (phrase == null || phrase.equals("")) {
            return null;
        } else {
            String[] phraseArray = Arrays
                    .stream(phrase.split(" "))
                    .map(JadenCase::capitalize)
                    .toArray(String[]::new);

            return String.join(" ", phraseArray);
        }
    }

}