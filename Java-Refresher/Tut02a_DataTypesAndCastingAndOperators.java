public class Tut02a_DataTypesAndCastingAndOperators {
  public static void main(String[] args) {
    int x = 8;
    double y = x; //automatic conversion via widening.
    System.out.println(x);
    System.out.println(y);

    double z = 9.0;
    int z2 = (int) z; //manual casting
    System.out.println(z);
    System.out.println(z2);
  }
}

//two types: primitive and non-primitive.
//primitive => byte, short, int, long, float, double, boolean, and char.
//non-primitive => string, arrays, classes.
//non-primitiive types are called reference types.
//non-primitive types can store null.
//two kinds of casting: widening & narrowing.
//widening is when we convert from small to larger type size: byte -> short -> char -> int -> long -> float -> double
//narrowing is large to smaller type size: double -> float -> long -> int -> char -> short -> byte
//widening is automatic & narrowing is manual.
//different types of operators; assingment, arithmetic, comparision, logical and bitwise.