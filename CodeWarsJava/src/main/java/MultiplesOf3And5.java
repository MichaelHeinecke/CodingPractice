public class MultiplesOf3And5 {

    public int solution(int number) {
        int result = 0;

        if (number == 0) {
            return result;
        }

        for (int i = 0; i < number; i++) {
            if (i % 3 == 0) {
                result += i;
            } else if (i % 5 == 0) {
                result += i;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        System.out.println(new MultiplesOf3And5().solution(-1));
    }

}