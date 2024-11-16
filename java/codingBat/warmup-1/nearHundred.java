public class nearHundred {
   public boolean NearHundred(int n) {
      return (Math.abs(100 - n) <= 10 ) || (Math.abs(200 - n) <= 10 );
   }
}
