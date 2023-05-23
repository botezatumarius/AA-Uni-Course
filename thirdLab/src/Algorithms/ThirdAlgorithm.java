package Algorithms;

import java.util.*;

public class ThirdAlgorithm {

    public static void findPrimes(int n) {
        boolean[] c = new boolean[n + 1];
        Arrays.fill(c, true);
        c[1] = false;
        int i = 2;
        while (i <= n) {
            if (c[i]) {
                int j = i + 1;
                while (j <= n) {
                    if (j % i == 0) {
                        c[j] = false;
                    }
                    j++;
                }
            }
            i++;
        }

    }

}
