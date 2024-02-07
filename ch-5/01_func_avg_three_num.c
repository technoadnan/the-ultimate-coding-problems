#include <stdio.h>


int avg(int n1, int n2,int n3);

int main(int argc, char const *argv[]) {
   printf("%d",avg(90,89,95));
   return 0;
   
}

int avg(int n1, int n2,int n3)
{
   return (n1 + n2 + n3) / 3;
}