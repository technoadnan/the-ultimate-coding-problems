
import java.util.Scanner;

public class StringE {
  public boolean stringE(String str) {
    int cnt = 0;
    for(int i=0; i<str.length(); i++) {
      if(str.charAt(i) == 'e') cnt++;
    }
    return (cnt >= 1 && cnt <= 3);
  }

  public static void main(String[] args) {
    try (Scanner scanner = new Scanner(System.in)) {
      System.out.print("Enter a string: ");
      String input = scanner.nextLine();
      StringE stringE = new StringE();
      boolean result = stringE.stringE(input);
      System.out.println("Result: " + result);
    }
  }
}
