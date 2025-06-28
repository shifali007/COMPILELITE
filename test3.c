#include <stdio.h>

// Small functions doing simple tasks

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int multiply(int a, int b) {
    return a * b;
}

int divide(int a, int b) {
    return b != 0 ? a / b : 0;
}

int mod(int a, int b) {
    return b != 0 ? a % b : 0;
}

int square(int a) {
    return a * a;
}

int cube(int a) {
    return a * a * a;
}

int max(int a, int b) {
    return a > b ? a : b;
}

int min(int a, int b) {
    return a < b ? a : b;
}

int is_even(int a) {
    return a % 2 == 0;
}

int is_odd(int a) {
    return a % 2 != 0;
}

int abs_val(int a) {
    return a < 0 ? -a : a;
}

int factorial(int n) {
    int f = 1;
    for (int i = 2; i <= n; i++) f *= i;
    return f;
}

int fibonacci(int n) {
    if (n <= 1) return n;
    int a = 0, b = 1, c;
    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

int sum_array(int arr[], int n) {
    int s = 0;
    for (int i = 0; i < n; i++) s += arr[i];
    return s;
}

int count_positive(int arr[], int n) {
    int c = 0;
    for (int i = 0; i < n; i++) if (arr[i] > 0) c++;
    return c;
}

int count_negative(int arr[], int n) {
    int c = 0;
    for (int i = 0; i < n; i++) if (arr[i] < 0) c++;
    return c;
}

int sum_even(int arr[], int n) {
    int s = 0;
    for (int i = 0; i < n; i++) if (arr[i] % 2 == 0) s += arr[i];
    return s;
}

int sum_odd(int arr[], int n) {
    int s = 0;
    for (int i = 0; i < n; i++) if (arr[i] % 2 != 0) s += arr[i];
    return s;
}

int find_max(int arr[], int n) {
    int m = arr[0];
    for (int i = 1; i < n; i++) if (arr[i] > m) m = arr[i];
    return m;
}

int find_min(int arr[], int n) {
    int m = arr[0];
    for (int i = 1; i < n; i++) if (arr[i] < m) m = arr[i];
    return m;
}

void reverse_array(int arr[], int n) {
    for (int i = 0; i < n / 2; i++) {
        int temp = arr[i];
        arr[i] = arr[n - i - 1];
        arr[n - i - 1] = temp;
    }
}

void print_array(int arr[], int n) {
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");
}

void increment_all(int arr[], int n) {
    for (int i = 0; i < n; i++) arr[i]++;
}

void decrement_all(int arr[], int n) {
    for (int i = 0; i < n; i++) arr[i]--;
}

void double_all(int arr[], int n) {
    for (int i = 0; i < n; i++) arr[i] *= 2;
}

void halve_all(int arr[], int n) {
    for (int i = 0; i < n; i++) arr[i] /= 2;
}

void zero_negatives(int arr[], int n) {
    for (int i = 0; i < n; i++) if (arr[i] < 0) arr[i] = 0;
}

void square_all(int arr[], int n) {
    for (int i = 0; i < n; i++) arr[i] *= arr[i];
}

void cube_all(int arr[], int n) {
    for (int i = 0; i < n; i++) arr[i] = arr[i] * arr[i] * arr[i];
}

int main() {
    int arr[10] = {1, -2, 3, -4, 5, -6, 7, -8, 9, -10};

    printf("Add: %d\n", add(5, 3));
    printf("Subtract: %d\n", subtract(10, 4));
    printf("Multiply: %d\n", multiply(2, 6));
    printf("Divide: %d\n", divide(20, 4));
    printf("Mod: %d\n", mod(17, 5));
    printf("Square: %d\n", square(6));
    printf("Cube: %d\n", cube(3));
    printf("Max: %d\n", max(12, 7));
    printf("Min: %d\n", min(12, 7));
    printf("Is Even: %d\n", is_even(8));
    printf("Is Odd: %d\n", is_odd(9));
    printf("Abs Val: %d\n", abs_val(-23));
    printf("Factorial: %d\n", factorial(5));
    printf("Fibonacci: %d\n", fibonacci(10));

    printf("Sum Array: %d\n", sum_array(arr, 10));
    printf("Count Positives: %d\n", count_positive(arr, 10));
    printf("Count Negatives: %d\n", count_negative(arr, 10));
    printf("Sum Even: %d\n", sum_even(arr, 10));
    printf("Sum Odd: %d\n", sum_odd(arr, 10));
    printf("Max in Array: %d\n", find_max(arr, 10));
    printf("Min in Array: %d\n", find_min(arr, 10));

    printf("Original Array:\n");
    print_array(arr, 10);

    increment_all(arr, 10);
    printf("After Increment:\n");
    print_array(arr, 10);

    decrement_all(arr, 10);
    printf("After Decrement:\n");
    print_array(arr, 10);

    double_all(arr, 10);
    printf("After Doubling:\n");
    print_array(arr, 10);

    halve_all(arr, 10);
    printf("After Halving:\n");
    print_array(arr, 10);

    zero_negatives(arr, 10);
    printf("After Zeroing Negatives:\n");
    print_array(arr, 10);

    square_all(arr, 10);
    printf("After Squaring:\n");
    print_array(arr, 10);

    cube_all(arr, 10);
    printf("After Cubing:\n");
    print_array(arr, 10);

    reverse_array(arr, 10);
    printf("After Reversing:\n");
    print_array(arr, 10);

    return 0;
}