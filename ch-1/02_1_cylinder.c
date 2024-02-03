#include <stdio.h>
#include <math.h>
 
const double PI = 3.14159265359; 
int main(int argc, char const *argv[])
{
   int radius, height;
   printf("Enter the radius ");
   scanf("%d",&radius);
   printf("Enter the height ");
   scanf("%d",&height);

   float result = PI * pow(radius,2) * height;
   printf("%f", result); // make sure to print this with double(more precendence)
   return 0;
}
