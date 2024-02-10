#include <stdio.h>

void times_10(int n);
int main(int argc, char const *argv[]) {
   int n = 9;
   times_10(39);
   return 0;
}

void times_10(int n)
{
   int *ptr = &n;
   int j = *ptr * 10;
   printf("%d", j);
}