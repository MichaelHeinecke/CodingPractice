package com.hackerrank.interview_preparation;

import java.io.IOException;

public class JumpingOnClouds {
    
    static int jumpingOnClouds(int[] c) {
        int jump = 0;

        for (int i = 0; i < c.length-1; i++) {
            jump++;
            if (i < c.length - 2 && c[i + 2] == 0) {
                i++;
            }
        }
        return jump;
    }

    public static void main(String[] args) throws IOException {
//        int[] n = new int[]{0, 1, 0, 0, 0, 1, 0};
        int[] n = new int[]{0, 0, 0, 0, 1, 0};

        int result = jumpingOnClouds(n);

        System.out.println(result);
    }
}
