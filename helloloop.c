#include <stdio.h>

int main() {

    int i;
    int entry_per_line = 5;

    for(i=0; i<=100; i++) {
        if(i % entry_per_line == 0) {
            printf("\n");
        }
        printf("%d ", i);
    }
    return 0;
}