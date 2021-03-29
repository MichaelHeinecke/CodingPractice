import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

public class FindOdd {
    public static int findIt(int[] a) {
        List<Integer> oddOccurrence = Arrays.stream(a).boxed()
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()))
                .entrySet().stream()
                .filter(entry -> entry.getValue() % 2 != 0)
                .map(Map.Entry::getKey)
                .collect(Collectors.toList());

        return oddOccurrence.get(0);
    }
}