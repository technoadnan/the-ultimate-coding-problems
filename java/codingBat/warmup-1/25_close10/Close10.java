

public class Close10 {
    public static int close10(int a, int b) {
        int aDiff = Math.abs(10-a); // 2
        int bDiff = Math.abs(10-b); // 3
        if(aDiff == bDiff) {
          return 0;
        }
        else if(aDiff > bDiff) {
          return b;
        }
        else{
          return a;
        }
      }
      
    public static void main(String[] args) {
        // Your code here
        close10(8, 13);
    }
}
