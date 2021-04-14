public class PigLatin {
    public static boolean isAlpha(String word) {
        return word.matches("[a-zA-Z]{2,}");
    }

    public static String pigIt(String str) {
        String[] words = str.split(" ");
        for (int idx = 0; idx < words.length; idx++) {
            if (isAlpha(words[idx])) {
                words[idx] = words[idx].substring(1) + words[idx].charAt(0) + "ay";
            }
        }

        return String.join(" ", words);
    }
}