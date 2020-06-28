import java.util.*;

class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Deque<String> guestNames = new LinkedList();

        for (int i = 0; i < 4; i++) {
            String inputNames = scanner.nextLine();
            List<String> names = Arrays.asList(inputNames.split(" "));
            guestNames.addAll(names);
        }

        Iterator descendingIterator = guestNames.descendingIterator();

        while (descendingIterator.hasNext()) {
            System.out.println(descendingIterator.next());
        }

    }
}