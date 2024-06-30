#include <stdio.h>

float convert_temp(float celcius);
int main(int argc, char const *argv[])
{
   float celcius;
   printf("Celcius: %.2f", convert_temp(4));

   return 0;
}

float convert_temp(float celcius)
{
   return ((celcius * 9/5) + 32);
}