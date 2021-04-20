public class DataReverse {
    public static int[] dataReverse(int[] data) {
        int[] reversedData = new int[data.length];
        for (int startIdx = data.length - 8; startIdx >= 0; startIdx -= 8) {
            for (int bitIdx = startIdx, targetIdx = data.length - startIdx - 8; bitIdx <= startIdx + 7; bitIdx++,
                    targetIdx++) {
                reversedData[targetIdx] = data[bitIdx];
            }
        }

        return reversedData;
    }
}
