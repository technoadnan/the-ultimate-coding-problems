#include <stdio.h>

typedef struct arrow_method
{
   int num;
   char name[20];
} arrow_method;


int main(int argc, char const *argv[]) {
   struct arrow_method s1;
   struct arrow_method *ptr;
   ptr = &s1;
   s1.num = 20;
   ptr->num = 10;
   printf("%d", s1.num);
   return 0;
   
}