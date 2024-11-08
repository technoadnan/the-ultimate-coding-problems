public class parrotTrouble {
   
   public boolean parrotTrouble(boolean talking, int hour) {
      // if  (7 > hour > 20) && (talking == true) {
      // if ((hour<7 || hour > 20) && talking == true){
      //   return true;
      // }
      // return false;
      return ((hour<7 || hour > 20) && talking == true);
  }
}