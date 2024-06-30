#include <stdio.h>

int main(int argc, char const *argv[]) {
   int a = 345;
   int *ptr; 
   int **ptr_ptr;

   ptr = &a; // adress of a
   ptr_ptr = &ptr; // adress of ptr -> adress of a
   
   printf("%d", **ptr_ptr);
   

   return 0;
}