import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

public class CountingDuplicates {

    public static long duplicateCount(String text) {
        if (text == null || text.length() < 2) {
            return 0L;
        }

        Map<Character, Long> charFrequency = text
                .chars()
                .map(Character::toLowerCase)
                .mapToObj(c -> (char) c)
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));

        return charFrequency.values().stream().filter(v -> v >= 2).count();
    }

}