public class Makes10 {

    public static boolean makes10(int a, int b) {
        return ((a == 10) || (b == 10) ) || a+b == 10;
      }

      public static void main(String[] args) {
        // Your code here
        int a = 12;
        int b = 4;
        makes10(a, b);
        
    }
}
