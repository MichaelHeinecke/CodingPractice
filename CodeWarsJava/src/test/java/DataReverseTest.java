import org.junit.Test;

import static org.junit.Assert.assertArrayEquals;

public class DataReverseTest {

    @Test
    public void Test() {
        int[] data1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
        int[] data2 = {8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7};
        assertArrayEquals(data2, DataReverse.dataReverse(data1));
    }

    @Test
    public void Test1() {
        int[] data1 = {1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0};
        int[] data2 = {1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1};
        assertArrayEquals(data2, DataReverse.dataReverse(data1));
    }

    @Test
    public void Test2() {
        int[] data1 = {0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1};
        int[] data2 = {0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0};
        assertArrayEquals(data2, DataReverse.dataReverse(data1));

    }
}