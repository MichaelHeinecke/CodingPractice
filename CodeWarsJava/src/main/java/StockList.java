import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

public class StockList {

    // 1st parameter is the stocklist (L in example),
    // 2nd parameter is list of categories (M in example)
    public static String stockSummary(String[] lstOfArt, String[] lstOf1stLetter) {
        String stockSummary = "";

        if (lstOf1stLetter.length == 0 || lstOfArt.length == 0) return stockSummary;

        Map<String, Integer> artQuantityMap = new HashMap<>();
        for (String k : lstOf1stLetter) {
            artQuantityMap.put(k, 0);
        }

        for (String e : lstOfArt) {
            String[] s = e.split(" ");
            if (Arrays.asList(lstOf1stLetter).contains(s[0].substring(0, 1))) {
                artQuantityMap.merge(s[0].substring(0, 1), Integer.parseInt(s[1]), Integer::sum);
            }
        }

        stockSummary = artQuantityMap.entrySet().stream()
                .map(e -> "(" + e.getKey() + " : " + e.getValue() + ")")
                .collect(Collectors.joining(" - "));

        return stockSummary;
    }
}
