#include <stdio.h>
#include <stdbool.h>

int main(){
  bool isProgrammingFun = true;
  bool isFistTasty = false;

  //using %d int format specifier for boolean values as they are really just 0 or non-zero integers.
  printf("%d\n", isProgrammingFun);
  printf("%d", isFistTasty);
  return 0;
}

//Notes:
//to use boolean true false values in c program must include the stdbool.h libary.
//decalred using the bool keyword.
//1 or any non-zero # = true.
//0 = false.