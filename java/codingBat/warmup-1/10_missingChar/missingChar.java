public class missingChar {
    public static void main(String[] args) {
        // s.c => o(n) // created a new string
  // t.c => o(n) // loop
  // String s = "";
  // for(int i = 0; i<str.length(); i++) {
  //   if(i != n) {
  //     s = s + str.charAt(i);
  //   }
  // }
  // return s;
  
  
  // t.c => o(1)
  // s.c => o(1)
  String front = str.substring(0,n);
  String back = str.substring(n+1, str.length());
  return front+back;
    }
}
