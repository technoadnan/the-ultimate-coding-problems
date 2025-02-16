public class Front3 {
    public String solution(String str) {
        String firstPortion = "";
        if (str.length() > 3){
          firstPortion = str.substring(0,3);
        }
        else{
          firstPortion = str;
        }
        
        // t.c -> o(1)
        // s.c -> o(1)
        
        return firstPortion + firstPortion + firstPortion;
        
        // t.c -> o(n)
        // s.c -> o(n)
        
        // String text = "";
        // int i = 3;
        // while(i > 0){
        //   text = text + firstPortion;
        //   i--;
        // }
        // return text;
        
        
      }
    public static void main(String[] args) {
        Front3 front3 = new Front3();
        String result = front3.solution("example");
        System.out.println(result);
    }
}
