#include <stdio.h>
void encrypt(char str[]);
int main(int argc, char const *argv[]) {

   char arr[] = "adnan";
   encrypt(arr);
   printf("%s\n",arr);

   return 0;
}

void encrypt(char str[])
{
   char *ptr = str;
   int i = 0;
   while (*ptr != '\0')
   {
      str[i] = *ptr+1;
      ptr++, i++;
   }
}


