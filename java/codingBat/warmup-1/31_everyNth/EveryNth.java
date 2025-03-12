public class EveryNth {
    public static String everyNth(String str, int n) {
        String newStr = "";
        for(int j = 0; j < str.length(); j++) {
          
          if((j % n)==0){
            newStr = newStr + str.charAt(j);
          }
      
        }
        return newStr;
      }
      
    public static void main(String[] args) {
        // Your code here
        String str = "Miracle";
        int n = 2;
        everyNth(str,n);
    }
}
