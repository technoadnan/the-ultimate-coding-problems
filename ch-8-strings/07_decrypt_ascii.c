#include <stdio.h>
void decrypt(char str[]);

int main(int argc, char const *argv[]) {
   char arr[] = "beobo";
   decrypt(arr);
   printf("%s",arr);
   return 0;
}
void decrypt(char str[])
{
   char *ptr = str;
   int i = 0;
   while (*ptr != '\0')
   {
      str[i] = *ptr-1;
      ptr++, i++;
   }
}

