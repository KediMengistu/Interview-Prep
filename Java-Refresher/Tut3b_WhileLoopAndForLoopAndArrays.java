public class Tut3b_WhileLoopAndForLoopAndArrays {
  public static void main(String[] args){
    int x = 5;
    while(x<5){
      x++;
    }
    int i = 0;
    do {
      System.out.println("In the do part of the do-while loop. Value of iterator i is: " + i);
      i++;
    }
    while(i < 5);

    for(int j=0; j<10; j++){
      System.out.println("Cycle number:" + " " + (j + 1) + " " + "In the for loop baby!");
    }
    for(int k=0; k<5; k++){
      for(int l=0; l<10; l++){
        System.out.println("In the nested for loop. K iteration: " +  k + ", L iteration: " + l);
      }
    }
    int[] nums = {1, 4, 5, 4, 2, 5, 4};
    for(int value: nums){
      System.out.println("value: " + value);
    }

    int[] newArray = new int[5];
    for(int value: newArray) {
      System.out.println(value);
    }
    //2d array.
    int[][] myNumbers = { {1, 2, 3, 4}, {5, 6, 7} };
    //use nested loops to iterate over the 2d array;
    for(int r=0; r<myNumbers.length; r++){
      for(int s=0; s<myNumbers[r].length; s++){
        System.out.println("[" + r + "," + s + "] = " + myNumbers[r][s]);
      }
    }
  }
}

//Notes:
//while loop will be executed while condition is true; make sure there is a terminating condition.
//do-while loop will at least be executed once as the do is executed before the while is.
//for loop structure: for(starter; loop condtion; incrementer){...}.
//for each loop used to iterate over lists/collections of elements.
//use break to break out of the entire loop and use continue to break out of current iteration onto the next.
//use arrays to store a collection of elements referenced by a single variable.
//use the .length property on arrays to get the number of elements in the array.
//can access element in array via indexing arr[indexValue].
//multi-diemensional arrays aka 2d arrays.