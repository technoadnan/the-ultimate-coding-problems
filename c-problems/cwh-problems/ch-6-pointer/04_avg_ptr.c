#include <stdio.h>

int sum(int n1, int n2);
int avg(int n1, int n2);

void sumAndAvg(int a, int b, int *sum, float *avg)
{
   *sum = a + b;
   *avg = (float)(*sum)/2;

}

int main(int argc, char const *argv[]) {
   // int s = sum(20,40);
   // printf("%d\n", s);

   // int a = avg(20,40);
   // printf("%d", a);

   int i, j, sum;
   float avg;

   i,j = 20,40;
   sumAndAvg(i,j,&sum, &avg);
   printf("The value of sum is %d \n", sum);
   printf("The value of sum is %.0f \n", avg);
   
   return 0;
}

int sum(int n1, int n2)
{
   int *ptr1 = &n1;
   int *ptr2 = &n2;
   int i,j = *ptr1 + *ptr2;

}
int avg(int n1, int n2)
{
   int *ptr1 = &n1;
   int *ptr2 = &n2;
   int i,j = (*ptr1 + *ptr2)/2;
}
