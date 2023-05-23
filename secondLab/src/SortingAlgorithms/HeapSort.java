package SortingAlgorithms;

public class HeapSort {
    public void heapSort(int[] arr, int start, int end) {
        int n = end - start + 1;
        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(arr, n, i, start);

        for (int i = n - 1; i >= 0; i--) {
            int temp = arr[start];
            arr[start] = arr[start + i];
            arr[start + i] = temp;
            heapify(arr, i, 0, start);
        }
    }

    private void heapify(int[] arr, int n, int i, int start) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if (left < n && arr[start + left] > arr[start + largest])
            largest = left;

        if (right < n && arr[start + right] > arr[start + largest])
            largest = right;

        if (largest != i) {
            int swap = arr[start + i];
            arr[start + i] = arr[start + largest];
            arr[start + largest] = swap;
            heapify(arr, n, largest, start);
        }
    }
}
