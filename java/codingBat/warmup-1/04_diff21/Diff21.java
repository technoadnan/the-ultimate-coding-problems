
public class Diff21 {

    public static void main(String[] args) {
        int n = 45;
        int sub = 21 - n;
        if (sub < 0) { // if sub is negative; converting to positive
            sub = sub * -1;
        }
        System.err.println((n > 21) ? sub * 2 : sub);
    }
}
