#include <stdio.h>

int sum_n_num(int n);

int main(int argc, char const *argv[]) {
   printf("%d", sum_n_num(10));
   return 0;
}

int sum_n_num(int n)
{
   if (n == 0) return 0;
   return n + sum_n_num(n-1);
}