#include <stdio.h>
typedef struct store_date
{
   int month, day, year, hour, min, second;
} sd;

int compare(sd d1, sd d2)
{
   if (d1.year > d2.year || d1.month > d2.month || d1.day > d2.day)
   {
      return 1;
   }
   if (d1.year<d2.year || d1.month < d2.month || d1.day < d2.day)
   {
      return -1;
   }

   if (d1.hour > d2.hour || d1.min > d2.min || d1.second > d2.second)
   {
      return 1;
   }
   if (d1.hour<d2.hour || d1.min < d2.min || d1.second < d2.second)
   {
      return -1;
   }

   return 0;
   
};


int main(int argc, char const *argv[]) {
   sd event1 = {10,29,2006};
   sd event2 = {10,29,2008};
   compare(event1, event2);
   printf("%d", compare(event1, event2));
   return 0;
}