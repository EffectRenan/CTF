public class Solve {
    
    public static void main(String[] args) {
        String input = "inagzgkpm)Wl&Tg&io";
        System.out.println(shift2(shift(input)));
    }
    
    public static String shift(String input) {
        String ret = "";
        for (int i = 0; i<input.length(); i++) {
            ret+=(char)(input.charAt(i)+i);
        }
        return ret;
    }
    public static String shift2(String input) {
        String ret = "";
        for (int i = 0; i<input.length(); i++) {
            ret+=(char)(input.charAt(i)-Integer.toString((int)input.charAt(i)).length());
        }
        return ret;
    }
    
    

}
