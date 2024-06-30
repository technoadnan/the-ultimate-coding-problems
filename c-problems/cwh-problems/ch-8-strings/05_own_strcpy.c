#include <stdio.h>


void copy(char target[], char source[]);
int main(int argc, char const *argv[])
{
   char str1[] = "adnan";
   char str2[10];
   copy(str2, str1);

   // int j = 0;
   // while (str1[j] != '\0')
   // {
   //    str2[j] = str1[j];
   //    j++;
   // }
   // str2[j] = '\0'; // add this to properly terminate the str

   printf("%s", str2);

   return 0;
}


void copy(char target[], char source[])
{
   int i = 0;
   while (source[i] != '\0')
   {
      target[i] = source[i];
      i++;
   }
   target[i] = '\0';
}


// #include <stdio.h>

// int main(int argc, char const *argv[]) {
//     const char str1[] = "adnan";
//     int i = 0;

//     while (str1[i] != '\0' && i < sizeof(str1) - 1) {
//         i++;
//     }

//     char str2[i + 1]; // Add 1 for the null terminator

//     int j = 0;
//     while (str1[j] != '\0') {
//         str2[j] = str1[j];
//         j++;
//     }

//     str2[j] = '\0'; // Null-terminate str2

//     printf("%s", str2);

//     return 0;
// }
