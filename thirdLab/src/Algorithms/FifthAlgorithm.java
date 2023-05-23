package Algorithms;

import java.util.*;

public class FifthAlgorithm {

    public static void findPrimes(int n) {
        boolean[] c = new boolean[n + 1];
        Arrays.fill(c, true);
        c[1] = false;
        int i = 2;
        while (i <= n) {
            int j = 2;
            while (j <= Math.sqrt(i)) {
                if (i % j == 0) {
                    c[i] = false;
                }
                j++;
            }
            i++;
        }

    }

}
