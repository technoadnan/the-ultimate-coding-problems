#include <stdio.h>
void printArray(int *ptr, int n)
{
   for (int i = 0; i < n; i++)
   {
      printf("The value of element %d is %d\n", i, *(ptr + i));
   }
}


// integer array 
void printArray(int ptr[], int n)
{
   for (int i = 0; i < n; i++)
   {
      printf("The value of element %d is %d\n", i+1, ptr[i]);
   }
   ptr[2] = 5555;
   
}

int main(int argc, char const *argv[]) {
   int marks[4];
   int *ptr;
   ptr = &marks[0]; // can be written as ptr = marks
   // printf("%u\n",ptr);
   // ptr = marks;
   // printf("%u",ptr);
   for (int i = 0; i < 4; i++)
   {
      printf("Enter the value of marks for student: %d: \n", i+1);
      scanf("%d", ptr);
      ptr++;
   }

   for (int i = 0; i < 4; i++)
   {
      printf("The value of marks for students %d is %d \n",i+1, marks[i]);
   }
   return 0;
}