package SortingAlgorithms;

public class RadixSort {

    public void radixSort(int[] arr) {
        // Find the maximum absolute value in the array
        int maxVal = Integer.MIN_VALUE;
        for (int i = 0; i < arr.length; i++) {
            if (Math.abs(arr[i]) > maxVal) {
                maxVal = Math.abs(arr[i]);
            }
        }

        // Perform radix sort on the two's complement representation of the integers
        int[] temp = new int[arr.length];
        for (int exp = 1; maxVal / exp > 0; exp *= 10) {
            int[] count = new int[10];

            // Count the occurrences of each digit
            for (int i = 0; i < arr.length; i++) {
                int digit = (Math.abs(arr[i]) / exp) % 10;
                count[digit]++;
            }

            // Compute the cumulative counts of each digit
            for (int i = 1; i < count.length; i++) {
                count[i] += count[i - 1];
            }

            // Build the sorted array by placing each element in the correct position
            for (int i = arr.length - 1; i >= 0; i--) {
                int digit = (Math.abs(arr[i]) / exp) % 10;
                int index = count[digit] - 1;
                temp[index] = arr[i];
                count[digit]--;
            }

            // Copy the sorted array back into the original array
            System.arraycopy(temp, 0, arr, 0, arr.length);
        }

        // Convert the sorted two's complement integers back to their original negative
        // representation
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] < 0) {
                arr[i] = ~(arr[i] - 1);
            }
        }
    }

}
