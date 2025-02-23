class Or35 {
    public static boolean or35(int n) {
        if(n > 0){
          if((n % 3 == 0) || (n % 5 == 0)){
            return true;
          }
        }
        return false;
      }
    public static void main(String[] args) {
        // Your code here
        System.out.println(or35(5));
    }
}
