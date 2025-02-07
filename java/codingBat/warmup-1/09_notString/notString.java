public String notString(String str) {
    // this will throw an err cuz what if the length is low
    // String notSubString = str.substring(0,3); // not

    if((str.length() >= 3 && str.substring(0, 3).equals("not"))){
        return str;
    }
    // if(notSubString.equals("not") && str.length() >= 3){
    //   return str;
    // }
    else{
        return "not "+str;
    }




    // String newStr = "not " + str;
    // if(str.equals(newStr)){ // str = not bad, newStr = not not bad
    //   return str;
    // }
    // else{
    //   return newStr;
    // }
}
