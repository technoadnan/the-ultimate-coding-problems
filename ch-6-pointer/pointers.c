#include <stdio.h>

int main(int argc, char const *argv[]) {
   int i = 8;
   int *j; // declare j as pointer
   j = &i;
   printf("%u\n", &i); // address of i
   printf("%u\n", j); // address of j's pointer
   printf("%u\n", &j); // address of j
   printf("%d\n", i); // value of i
   printf("%d\n", *(&j)); // 
   
   int a = 10;
   int *ptr = &a;
   printf("%u\n", ptr);
   printf("%d\n", *ptr);


   return 0;
}