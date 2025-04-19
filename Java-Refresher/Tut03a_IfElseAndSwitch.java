public class Tut03a_IfElseAndSwitch {
  public static void main(String[] args) {
    int x = (5 < 25) ? 5 : 25;
    System.out.println(x);
  }
}

//Notes:
//if...else if...else.
//shorthand notation via (condition) ? result if true : result if false.
//switch statement works like so....
/*
 * switch (expression){
 *  case value:
 *    block of code
 *    break
 *  case value:
 *    block of code
 *    break
 *  default:
 *    block of code
 * }
 */
//whatever case value the expression matches will have it's code block run.
//default is the case matched if no other cases are matched.
//use break to exit the switch statement.


