import java.util.List;

public class SmileFaces {

    public static int countSmileys(List<String> smileList) {
        return (int) smileList.stream()
                .filter(face -> face.matches("[:;][-~]?[)D]"))
                .count();
    }
}