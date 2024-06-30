#include <stdio.h>

void func(int i);
int main(int argc, char const *argv[]) {
   int i=0;
   int *adress = &i;
   printf("%u\n",adress);
   func(i);
   return 0;
}

void func(int i) 
{
   int *j = &i;
   printf("%u\n",j);
}

// The adress is not because i was passed through an argument
