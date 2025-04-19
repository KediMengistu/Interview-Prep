#include <stdio.h>
#include <stdbool.h>

int main(){
  int x = 0;
  x = 10;
  if(x < 10){
    printf("x is less than 10, where the value of x is %d\n", x);
  }
  else if(x == 10){
    printf("x is equal to 10, where the value of x is %d\n", x);
  }
  else{
    printf("x is greater than 10, where the value of x is %d\n", x);
  }
  int result = (x != 10) ? 100 : 10;
  printf("result shows that x is not eqaul to 10 by displaying 100 and that it is eqaul to 10 by displaying 10 - result: %d\n", result);

  switch(x){
    case 0:
      printf("case 0, where x is 0 executes.\n");
      break;
    case 1:
      printf("case 1, where x is 1 executes.\n");
      break;
    case 10:
      printf("case 10, where x is 10 executes.\n");
      break;
    default:
      printf("default case where where x is not 0, 1, or 10 executes. x is %d\n", x);
      break;
  }

  return 0;
}

//Notes:
//shorthand if-else branch is (condition) ? result if true : result if not true.
//switch - match case to result of switch expression and execute corresponding case code.