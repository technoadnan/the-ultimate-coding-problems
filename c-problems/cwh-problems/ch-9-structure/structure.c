#include <stdio.h>
#include <string.h>

struct employee
{
   int code;
   float salary;
   char name[10];
};

// shorter way to make structure
typedef struct student
{
   char name[20];
   int marks;
}student;// now this value will be call


int main(int argc, char const *argv[]) {

   struct employee facebook[100];
   facebook[0].code = 100;
   facebook[0].salary = 10320.43;
   strcpy(facebook[0].name, "Bin");

   struct employee e1;
   e1.code = 100;
   e1.salary = 345.34;
   strcpy(e1.name, "Adnan");
   
   struct employee e2;
   e2.code = 2300;
   e2.salary = 415.4;
   strcpy(e2.name, "Alam");
   
   // using pointer
   struct employee e3;
   struct employee *ptr;
   ptr = &e3;
   (*ptr).code=101;
   ptr->code=201; // same as the v1 one 
   // printf("%d",e3.code);

   // shorter way to make structure
   student adnan;
   strcpy(adnan.name, "Adnan");
   adnan.marks = 34;
   printf("%s\n", adnan.name);
   printf("%d\n", adnan.marks);
    
   return 0;
}
