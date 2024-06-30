#include <stdio.h>

int main(int argc, char const *argv[])
{
   float celcius;
   printf("Celcius: ");
   scanf("%f", &celcius);

   printf("Farenheit: %.2f", ((celcius * 9/5) + 32));
   
   return 0;
}
