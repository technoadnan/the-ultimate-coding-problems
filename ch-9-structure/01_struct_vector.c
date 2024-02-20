#include <stdio.h>

typedef struct vectors
{
   int x;
   int y;
} vector;

struct vectors sumVectors(vector v1, vector v2)
{
   struct vectors result;
   result.x = v1.x + v2.x;
   result.y = v1.y + v2.y;
   return result;
};



int main(int argc, char const *argv[]) {
   vector first, second, sum;
   first.x = 30;
   first.y = 90;
   printf("X dim is %d and Y dim is %d\n", first.x, first.y);
   second.x = 130;
   second.y = 190;
   printf("X dim is %d and Y dim is %d\n", second.x, second.y);

   sum = sumVectors(first, second);
   printf("x sum is %d and y sum is %d", sum.x, sum.y); 


   
   return 0;
}