#include <stdio.h>
#include <string.h>

typedef struct salary_empl
{
   char name[20];
   int salary;
} empInfo;


int main(int argc, char const *argv[]) {
   empInfo name1;
   printf("Enter the name: ");
   scanf(strcpy(name1.name,"%s"),&name1.name);
   printf("Enter the salary: ");
   scanf("%d",&name1.salary);

   empInfo name2;
   printf("Enter the name: ");
   scanf(strcpy(name2.name,"%s"),&name2.name);
   printf("Enter the salary: ");
   scanf("%d",&name2.salary);

   FILE *fptr;
   fptr = fopen("salary_empl.txt","w");
   fprintf(fptr,"%s, %d\n%s, %d ",name1.name,name1.salary,name2.name,name2.salary);
   fclose(fptr);

   return 0;
}