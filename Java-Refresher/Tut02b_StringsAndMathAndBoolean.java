public class Tut02b_StringsAndMathAndBoolean {
  public static void main(String[] args) {
    String x = "hello";
    System.out.println(x);
    System.out.println(x.length());
    System.out.println(x.toUpperCase());
    System.out.println(x.indexOf("h")); //indexOf string version.
    System.out.println(x.indexOf('h'));  //indexOf char version.
    String y = "world";
    System.out.println(x + " " + y);
    System.out.println(x + " " + y + " " + 2);

    Math.min(5, 4);
    int a = 77;
    int b = 78;
    System.out.println(a > b); // will print the boolean value that is true or false - should be false in this case.
  }
}

//as reference types, strings have a set of methods that can be used to extract information from them.
//length shows the number of charachters.
//concatenation occurs when adding two strings or adding some other primitive data type to strings, where the result is a string comibining the two values.
//the \ allows for special characters to be included in the string. \", \'. \\
//the Java Math class allows you to perform a series of math operations.
//boolean is either true or false.