import java.util.Random;

import SortingAlgorithms.HeapSort;

public class RandomArray {

    public static int[] generateRandomArray(int min, int max, int size) {
        int[] arr = new int[size];
        Random rand = new Random();
        for (int i = 0; i < size; i++) {
            arr[i] = rand.nextInt(max - min + 1) + min;
        }
        return arr;
    }

    public static int[] generateSortedHalfRandomArray(int min, int max, int size) {
        int[] arr = generateRandomArray(min, max, size);
        HeapSort heapSort = new HeapSort();
        heapSort.heapSort(arr, 0, arr.length / 2);
        return arr;
    }
}
