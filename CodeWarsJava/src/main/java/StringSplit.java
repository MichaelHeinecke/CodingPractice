public class StringSplit {
    public static String[] solution(String s) {
        if (s.length() % 2 != 0) {
            s += "_";
        }

        String[] splitArray = new String[s.length() / 2];


        for (int idx = 0, start = 0; start <= s.length() - 2; idx++, start += 2) {
            splitArray[idx] = s.substring(start, start + 2);
        }

        return splitArray;
    }
}