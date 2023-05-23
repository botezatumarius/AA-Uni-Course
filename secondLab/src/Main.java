import java.util.Arrays;

import SortingAlgorithms.HeapSort;
import SortingAlgorithms.MergeSort;
import SortingAlgorithms.QuickSort;
import SortingAlgorithms.RadixSort;

public class Main {
    public static void main(String[] args) {
        System.out.print("\033[H\033[2J");
        System.out.flush();

        Main main = new Main();
        main.test1(10, false);
        main.test1(100, false);
        main.test1(10000, false);
        main.test1(100000, false);
        System.out.println("======================================");
        main.test1(10, true);
        main.test1(100, true);
        main.test1(10000, true);
        main.test1(100000, true);
    }

    public void test1(int range, boolean partialSort) {
        if (partialSort)
            System.out.println("Partially sorted arrays of randomly distributed integers between 0-" + range);
        else
            System.out.println("Unsorted arrays of randomly distributed integers between 0-" + range);

        QuickSort sort1 = new QuickSort();
        MergeSort sort2 = new MergeSort();
        HeapSort sort3 = new HeapSort();
        RadixSort sort4 = new RadixSort();
        for (int i = 100; i <= 100000; i *= 10) {
            int[] arr;

            if (partialSort)
                arr = RandomArray.generateRandomArray(0, range, i);
            else
                arr = RandomArray.generateSortedHalfRandomArray(0, range, i);

            int[] arr2 = arr.clone();
            long startTime = System.nanoTime();
            System.out.println("Elements in array: " + i);
            sort1.quickSort(arr2, 0, arr.length - 1);
            long endTime = System.nanoTime();
            double timeElapsed = (endTime - startTime) / 1_000_000_000.0;
            System.out.print(" Quick sort: " + timeElapsed);
            arr2 = arr.clone();
            startTime = System.nanoTime();
            sort2.mergeSort(arr2, 0, arr.length - 1);
            endTime = System.nanoTime();
            timeElapsed = (endTime - startTime) / 1_000_000_000.0;
            System.out.print(" Merge sort: " + timeElapsed);
            arr2 = arr.clone();
            startTime = System.nanoTime();
            sort3.heapSort(arr2, 0, arr.length - 1);
            endTime = System.nanoTime();
            timeElapsed = (endTime - startTime) / 1_000_000_000.0;
            System.out.print(" Heap sort: " + timeElapsed);
            arr2 = arr.clone();
            startTime = System.nanoTime();
            sort4.radixSort(arr2);
            endTime = System.nanoTime();
            timeElapsed = (endTime - startTime) / 1_000_000_000.0;
            System.out.println(" Radix sort: " + timeElapsed);
        }
        System.out.println();
    }
}
