#include <stdio.h>

int main(int argc, char const *argv[]) {
   int arr[10]= {1,2,3,4,5,6,7,8,9,10};
   int *ptr = &arr[0];
   ptr = ptr + 2;
   printf("%u", *ptr);
   
   return 0;
}