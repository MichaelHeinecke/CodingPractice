import org.junit.Test;

import static org.junit.Assert.assertArrayEquals;

public class DeadFishTest {
    @Test
    public void test1() {
        assertArrayEquals(new int[]{8, 64}, DeadFish.parse("iiisdoso"));
    }

    @Test
    public void test2() {
        assertArrayEquals(new int[]{8, 64, 3600}, DeadFish.parse("iiisdosodddddiso"));
    }

    @Test
    public void testInvalidCharacters() {
        assertArrayEquals(new int[]{8, 64, 3600}, DeadFish.parse("abciiisdosodddddisoabc"));
    }
}
