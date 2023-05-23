import Algorithms.*;

public class Main {
    public static void main(String[] args) {
        int[] ns = { 100, 1000, 6000, 15000, 25000, 50000, 100000, 200000, 500000 };
        for (int n : ns) {
            long start, end;
            double timeElapsed;

            System.out.println("n = " + n);

            // Fifth Algorithm
            start = System.nanoTime();
            FifthAlgorithm.findPrimes(n);
            end = System.nanoTime();
            timeElapsed = (end - start) / 1_000_000_000.0;
            System.out.println("Fifth Algorithm: " + timeElapsed + " seconds");

            // Second Algorithm
            start = System.nanoTime();
            SecondAlgorithm.findPrimes(n);
            end = System.nanoTime();
            timeElapsed = (end - start) / 1_000_000_000.0;
            System.out.println("Second Algorithm: " + timeElapsed + " seconds");

            // Third Algorithm
            start = System.nanoTime();
            ThirdAlgorithm.findPrimes(n);
            end = System.nanoTime();
            timeElapsed = (end - start) / 1_000_000_000.0;
            System.out.println("Third Algorithm: " + timeElapsed + " seconds");

            // Fourth Algorithm
            start = System.nanoTime();
            FourthAlgorithm.findPrimes(n);
            end = System.nanoTime();
            timeElapsed = (end - start) / 1_000_000_000.0;
            System.out.println("Fourth Algorithm: " + timeElapsed + " seconds");

            // First Algorithm
            start = System.nanoTime();
            FirstAlgorithm.findPrimes(n);
            end = System.nanoTime();
            timeElapsed = (end - start) / 1_000_000_000.0;
            System.out.println("First Algorithm: " + timeElapsed + " seconds");

            System.out.println();
        }
    }
}
