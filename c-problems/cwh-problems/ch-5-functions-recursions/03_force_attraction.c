#include <stdio.h>

float calc_gravitional_force(float m);
int main(int argc, char const *argv[]) {
   float m;
   printf("Enter the mass: ");
   scanf("%f", &m);

   printf("%.2f", calc_gravitional_force(m));
   
   return 0;
}

float calc_gravitional_force(float m)
{
   return m * 9.8;
}