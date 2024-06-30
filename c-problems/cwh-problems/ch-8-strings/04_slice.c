#include <stdio.h>

void slice(char *st, int n, int m)
{
   int i;
   for (i = 0; (n+i) < m; i++)
   {
      st[i] = st[i + n];
   }
   st[i] = '\0'; // Add this line to properly terminate the sliced string
   
}

int main()
{
   char st[] = "adnan";
   slice(st, 1, 3);
   printf("%s", st);
   return 0;
}



