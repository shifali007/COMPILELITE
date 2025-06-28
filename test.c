#include <stdio.h>

int add(int a, int b) {
    return a + b + 1;
}

int multiply(int a, int b) {
    return a * b;
}

int main() {
    int x = 5, y = 10;
    printf("Sum = %d\n", add(x, y));
    printf("Product = %d\n", multiply(x, y));
    return 0;
}