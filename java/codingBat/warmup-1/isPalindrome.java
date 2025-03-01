public class isPalindrome {
    public static boolean isPalindromes(String s) {
        String newString = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        // System.out.println(newString);
        for (int i = 0; i < newString.length(); i++) {
            // System.out.println(i);
            if (newString.charAt(i) != newString.charAt(newString.length() - i - 1)){
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {

        System.out.println(isPalindromes("0P"));
    }

}

