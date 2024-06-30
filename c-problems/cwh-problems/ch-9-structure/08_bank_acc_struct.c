#include <stdio.h>
#include <string.h>
typedef struct bank_acc_struct
{
   int acc_num;
   int money;
   char acc_holder_name[30];

} bank_info;


int main(int argc, char const *argv[]) {
   bank_info user1;
   user1.acc_num = 3456556;
   user1.money = 3456556;
   strcpy(user1.acc_holder_name, "Adnan");

   printf("Account number %d, name %s have %d$", user1.acc_num, user1.acc_holder_name, user1.money);
   return 0;
}