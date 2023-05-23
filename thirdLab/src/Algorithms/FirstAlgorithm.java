package Algorithms;

import java.util.*;

public class FirstAlgorithm {

    public static void findPrimes(int n) {
        boolean[] c = new boolean[n + 1];
        Arrays.fill(c, true);
        c[1] = false;
        int i = 2;
        while (i <= n) {
            if (c[i]) {
                int j = 2 * i;
                while (j <= n) {
                    c[j] = false;
                    j += i;
                }
            }
            i++;
        }
    }

}
