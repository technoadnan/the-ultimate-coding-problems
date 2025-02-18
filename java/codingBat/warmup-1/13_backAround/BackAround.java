public class BackAround {
    public String solution(String str) {
        // char front = str.charAt(0);
        char back = str.charAt(str.length()-1);
        
        return back + str + back;
      
        
        
      }
    public static void main(String[] args) {
        // Your code here
        BackAround solution = new BackAround();
        System.out.println(solution.solution("adnan"));

    }
}
