import java.util.*;

public class breakable_solve
{
    public static void main(String args[]) {
        check();
    }
    
    public static void check() {
        String flag = "k33p_1t_in_pl41n";
        String input = "ÒdÝ¾¤¤¾ÙàåÐcÝÆ¥ÌÈáÏÜ¦aã";
        String theflag = "";
        int i = 0;

        
        String hacked = "";
        for(i = 0; i < 16-2; i++){
            int crack = (int)(input.charAt(i));
            int key = (int)(flag.charAt(i));
            int j = 0;
            for(j = 0; j < 1000; j++) {
                if(key + j == crack) {
                    hacked += (char)(j);
                }
            }
        }
        String hacked2 = "";
        int count = 2;
        for(i = 16-2; i < input.length(); i++){
            int crack = (int)(input.charAt(i));
            int key = (int)(flag.charAt(count));
            int j = 0;
            for(j = 0; j < 1000; j++) {
                if(key + j == crack) {
                    hacked2 += (char)(j);
                }
            }
            count++;
        }
        
        System.out.println("Flag: rtcp{" + hacked2.charAt(0) + hacked2.charAt(1) + hacked + "}");

    }
}
