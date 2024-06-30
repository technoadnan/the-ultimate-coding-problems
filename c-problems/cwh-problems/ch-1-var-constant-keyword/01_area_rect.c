#include <stdio.h>

int main(int argc, char const *argv[])
{
   // Area of a rectangle
   int length, width;
   printf("Enter the length "); 
   scanf("%d",&length);
   printf("Enter the width ");
   scanf("%d",&width);

   printf("The area of the given rectangle is %d",length * width);
   
}
