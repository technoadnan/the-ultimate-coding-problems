public class EndUp {
    public static String endUp(String str) {
        // String newStr = "";
        if (str.length()<3){
          return str.toUpperCase();
        }
        return str.substring(0,str.length()-3) + str.substring(str.length()-3,str.length()).toUpperCase();
      }
    public static void main(String[] args) {
        // Your code here
        String str = "hi thERE";
        endUp(str);
    }
}
