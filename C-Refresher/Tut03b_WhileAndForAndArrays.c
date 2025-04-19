#include <stdio.h>
#include <stdbool.h>

int main(){
  int i = 0;
  while(i<5){
    printf("Value of i: %d\n", i);
    i++;
  }
  int j = 0;
  do {
    printf("Value of j: %d\n", j);
    j++;
  }
  while(j < 5);
  for(int h=0; h<5; h++){
    printf("Value of h: %d\n", h);
  }
  for(int k=0; k<5; k++){
    for(int g=0; g<5; g++){
      printf("Value of k: %d and g: %d\n", k, g);
    }
  }

  int myArray[] = {10, 20, 30, 40};
  int firstElement = myArray[0];
  printf("first value: %d\n", firstElement);
  myArray[0] = 99;
  printf("changed first value: %d\n", myArray[0]);
  printf(" %lu\n", sizeof(myArray)); //returns the size of the array in bytes; 4 bytes * 4 entries = 16 bytes which is returned.
  printf(" %lu\n", sizeof(myArray) / sizeof(myArray[0]));
  int length = sizeof(myArray) / sizeof(myArray[0]);
  for(int index=0; index<length; index++){
    printf("Value of myArray entry is: %d\n", myArray[index]);
  }
  printf("----------------------------------------------------------------------\n");
  int my2DArray[2][3] = {{1, 2, 3}, {4, 5, 6}}; //number of rows & number of coloums.
  for(int row=0; row<2; row++){
    for(int col=0; col<3; col++){
      printf("Value of my2DArray entry is: %d\n", my2DArray[row][col]);
    }
  }
  return 0;
}

//Notes:
//breaks used to break out of entire loops and continue is used to breack out the current iteration.
//to extract length of array in c use sizeof operator.