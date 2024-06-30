#include <stdio.h>

typedef struct complexNum
{
   int number;
   int complex;
} cm;

void display(cm c)
{
   printf("Real %d\n", c.number);
   printf("Imginary %d\n", c.complex);
}

int main(int argc, char const *argv[]) {
   cm cnums[5];
   for (int i = 0; i < 5; i++)
   {
      printf("Real: ");
      scanf("%d", &cnums[i].number);
      printf("Imginary: ");
      scanf("%d", &cnums[i].complex);
   }
   for (int i = 0; i < 5; i++)
   {
      display(cnums[i]);
   }
   
   return 0;
}