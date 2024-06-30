#include <stdio.h>

int main(int argc, char const *argv[]) {
   int a = 3;
   // a++ postFix, upt val after 
   // ++a prefix, upt val immediately
   printf("%d %d %d", a, ++a, a++); 
   // compiler execute lines from right to left


   return 0;
}