#include <stdio.h>

int main(int argc, char const *argv[]) {
   int a = 10;
   int *ptr = &a;
   printf("%u\n", ptr);
   printf("%d\n", *ptr);
   return 0;
}