public class Max1020 {
    public static int max1020(int a, int b) {
        int max1 = 0;
        int max2 = 0;
        // if(a > b) {
        //   if(a >= 10 && a <= 20){
        //     max = a;
        //   }
        // }
        // else{
        //   if(b >= 10 && b <= 20){
        //     max = b;
        //   }
        // }
        // if(max == 0) {
        //   return 0;
        // }
        // return max;
        if(a >= 10 && a <= 20){
          max1 = a;
        }
        if(b >= 10 && b <= 20) {
          max2 = b;
        }
        if(max1 > max2) {
          return a;
        }
        else if(max2 > max1){
          return b;
        }
        return 0;
      }
      
    
    public static void main(String[] args) {
        // Your code here
        max1020(11, 19);
    }
}
