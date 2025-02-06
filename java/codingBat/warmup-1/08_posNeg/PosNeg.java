public class PosNeg {
    public boolean posNeg(int a, int b, boolean negative) {
        // 2 int val
        // 1 is neg and 2 is pos then true
        // + - -> true
        // - - and parameter is true then true
        // if()

        int prod = a * b;
        if(negative){
            return a < 0 && b < 0;
        }
        else{
            return prod < 0;
        }
    }
    public static void main(String[] args) {
        // Your code here
        PosNeg posNeg = new PosNeg();
//        posNeg(1, -1, false) → true
//        posNeg(-1, 1, false) → true
//        posNeg(-4, -5, true) → true
        posNeg.posNeg(1,-1,false);
    }
}
