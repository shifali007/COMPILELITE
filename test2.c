#include <stdio.h>

// Function to print an array
void printArray(int arr[], int size) {
    for(int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

// Bubble Sort
void bubbleSort(int arr[], int size) {
    for(int i = 0; i < size - 1; i++) {
        for(int j = 0; j < size - i - 1; j++) {
            if(arr[j] > arr[j+1]) {
                // Swap
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

// Selection Sort
void selectionSort(int arr[], int size) {
    for(int i = 0; i < size - 1; i++) {
        int minIndex = i;
        for(int j = i + 1; j < size; j++) {
            if(arr[j] < arr[minIndex])
                minIndex = j;
        }
        // Swap
        int temp = arr[minIndex];
        arr[minIndex] = arr[i];
        arr[i] = temp;
    }
}

// Insertion Sort
void insertionSort(int arr[], int size) {
    for(int i = 1; i < size; i++) {
        int key = arr[i];
        int j = i - 1;
        while(j >= 0 && arr[j] > key) {
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = key;
    }
}

int main() {
    int data1[] = {64, 34, 25, 12, 22, 11, 90};
    int data2[] = {64, 34, 25, 12, 22, 11, 90};
    int data3[] = {64, 34, 25, 12, 22, 11, 90};
    int size = sizeof(data1) / sizeof(data1[0]);

    printf("Original array:\n");
    printArray(data1, size);

    bubbleSort(data1, size);
    printf("\nBubble Sorted array:\n");
    printArray(data1, size);

    selectionSort(data2, size);
    printf("\nSelection Sorted array:\n");
    printArray(data2, size);

    insertionSort(data3, size);
    printf("\nInsertion Sorted array:\n");
    printArray(data3, size);
    return 0;
}