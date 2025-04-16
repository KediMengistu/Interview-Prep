#include <stdio.h>

int main() {
  float myFloatNum = 3.5;
  printf("%f\n", myFloatNum);
  printf("%.1f\n", myFloatNum);
  printf("%.2f\n", myFloatNum);
  printf("%.4f\n", myFloatNum);

  //not recommeded to use %d when using sizeof operator, as long unsigned integer is expected output datatype from sizeof.
  //printf("size of myFloatNum variable: %d", sizeof(myFloatNum));
  printf("size of myFloatNum variable: %lu\n", sizeof(myFloatNum));

  //this is implicit type conversion; automatically occurs.
  //converts int 9 to float 9.000000.
  float x = 9;
  printf("x: %f\n", x);

  //converts float 9.99 to int 9.
  int x2 = 9.99;
  printf("x2: %d\n", x2);

  //unexpected output of 2.000000 - need to use explicit conversion where we convert the 5 and 2 to floating point inorder to keep the decimal value.
  // float divResult = 5 / 2;
  float divResult = (float) 5 / 2;
  printf("%.1f", divResult);
  return 0;
}

//Notes:
//4 basic data types, each corresponding to a specific size.
//int = whole numbers without decimals = 2 or 4 bytes.
//float = fractional numbers (sufficient for 6-7 decimal digits) = 4 bytes.
//double = fractional numbers (sufficient for 15 decimal digits) = 8 bytes.
//char = single characters, letters, numbers, or ASCII values = 1 byte.
//use .value to state the level of precision of the floating point or double variable to what you want; .2 = 2 decimal spots, .3 = 3 decimal spots, .4 = 4 decimal spots.
//sizeof operator allows us to view the number of spots in memory are dedicated to storing the value for that value.
//type conversion is used to convert the types in such a way to get the expected output.
//2 types: implicit and explicit conversion.
//implicit is automatic and explicit is manual.
//const denotes constant variables, where they are not able to change their value.
//operator types: arithmetic, assingment, comparison, logical, and bitwise.
