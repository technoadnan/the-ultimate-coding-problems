public class IntMax {
    public static int intMax(int a, int b, int c) {
        int high = 0;
        if(a > b){
            high = a;
        }
        else{
            high = b;
        }
        if(high > c){
            return high;
        }
        return c;
    }
    public static void main(String[] args) {
        // Your code here
        intMax(1, 2, 3);
    }
}
