#include <stdio.h>

int main() {
  int myNum = 15;
  int myNum2;
  myNum2 = 15;
  //error-bound.
  //printf(myNum2);
  printf("myNum2: %d \n", myNum2);
  printf("value: %d \n", 4);
  char var = 'a';
  printf("character variable: %c \n", var);
  char a = 65, b = 66, c = 67;
  printf("ascii a: %c\n", a);
  printf("ascii b: %c\n", b);
  printf("ascii c: %c\n", c);
  return 0;
}

//notes:
//variables cannot be printed; must be formatted via format specifiers to be printed.
//these inlude specifying the type of data that the variable/value corresponds to within the printf statement.
//each data-type corresponds to a unique format specifier.
//int => %d or %i
//float => %f or %F
//double => %lf
//char  => %c
//string => %s
//char is a single character and uses ''.
//char also correspond to ascii characters.