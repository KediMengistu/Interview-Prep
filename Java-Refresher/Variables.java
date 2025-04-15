public class Variables {
  public static void main(String[] args) {
    String name = "John";
    System.out.println(name);
    int myNum = 15;
    System.out.println(myNum);
    int myNum2;
    myNum2 = 16;
    System.out.println(myNum2);
    final int myNum3 = 17;
    System.out.println(myNum3);
    System.out.println("The values for the variables are as follows: myNum=" + myNum + ", myNum2=" + myNum2 + ", myNum3=" + myNum3);
    int x = 5, y = 6, z = 50;
    System.out.println(x + y + z);
    int x2, y2, z2;
    x2 = y2 = z2 = 50;
    System.out.println(x2 + y2 + z2);
  }
}

//Notes:
//Variables in java are container's used to store a value of some specific type.
//different types include string, int, double, char, boolean.
//variables declared as final cannot be overwritten.
//+ can be used to concatenate strings with other strings or with variables or data that are of other non-string types.
//can initialize variables in groups via a comma seperated list or can do so by assigning them all to be the same value.