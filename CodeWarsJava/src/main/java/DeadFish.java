import java.util.List;
import java.util.stream.Collectors;

public class DeadFish {
    public static int[] parse(String data) {
        if (data == null || data.isEmpty()) {
            return new int[]{};
        }

        // parse string; initial value 0; i increments value by 1; d decrements value;
        // s squares the value; o outputs the value into return array; ignore invalid characters
        int count = (int) data.chars().filter(c -> c == 'o').count();
        int[] returnArray = new int[count];

        List<Character> characterList = data.chars()
                .mapToObj(c -> (char) c)
                .filter(c -> c == 'i' || c == 'd' || c == 's' || c == 'o')
                .collect(Collectors.toList());

        int result = 0;
        int returnArrayIndex = 0;

        for (Character c : characterList) {
            switch (c) {
                case 'i':
                    result++;
                    break;
                case 'd':
                    result--;
                    break;
                case 's':
                    result = (int) Math.pow(result, 2);
                    break;
                case 'o':
                    returnArray[returnArrayIndex++] = result;
                    break;
                default:
                    break;
            }
        }

        return returnArray;
    }
}