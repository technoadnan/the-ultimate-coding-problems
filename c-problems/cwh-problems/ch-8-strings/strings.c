#include <stdio.h>
#include <string.h>
int main(int argc, char const *argv[]) {
   // char str[] = {'A','D','N','A','N'};
   char str[] = "Adnan Bin Alam";
   int size = sizeof(str) -1;

   for (int i = 0; i < size; i++)
   {
      printf("%c", str[i]);
   }printf("\n");

   // pointer
   char *ptr = str;
   while (*ptr != '\0')
   {
      printf("%c", *ptr);
      ptr++;
   }printf("\n");
   
   printf("%s\n",str); // easiest way

   // inputs 
   char st[50];
   scanf("%s", st);
   printf("%s", st);

   // puts and gets 
   // gets --> get the item
   // puts --> print the item 
   char s[51];
   fgets(s, sizeof(s), stdin);
   puts(s);

   // Important facts 
   char *ptr1 = "Adnan";
   ptr1 = "Alam"; // ptr1's value change to Alam b/c direct pointer
   char ptr2[] = "Adnan";
   // ptr2 = "Hello"; // can't change the value it if is ptr2[] 
   printf("%s", ptr2);

   // important methods 
   int strs = "Hello";
   int length = strlen(strs); // len
   printf("%d", length);
   
   char source[] = "Harry";
   char target[30];
   strcpy(target, source); // contains source

   char first_name[] = "hello";
   char *last_name = "World";
   strcat(first_name,last_name);
   printf("%s", first_name);

   // strcmp 

   return 0;
}