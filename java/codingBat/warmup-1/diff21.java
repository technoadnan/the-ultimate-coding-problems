public class Diff21 {
   public int diff21(int n) {
      int sub = 21 - n;
      if (sub < 0) { // if sub is negative; converting to positive
        sub = sub * -1;
      }
      return (n > 21) ? sub *2 : sub;
      
      
    }
    
}
