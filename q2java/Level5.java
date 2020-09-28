import java.util.Scanner;
import java.lang.Math;
public class Level5 {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        String[] adjArray = new String[5];
        String[] nounArray = new String[5];
        int numadj=keyboard.nextInt();
        int numnouns =keyboard.nextInt();
        for (int i = 0; i < numadj; i++) 
            adjArray[i]=keyboard.next();
        for (int j = 0; j < numnouns; j++) 
            nounArray[j]=keyboard.next();
        for (int i = 0; i < numadj; i++) {
            System.out.println();
            for (int j = 0; j < numnouns; j++) 
                System.out.println("i="+i+" j="+j+" "+adjArray[i]+" as "+nounArray[j]);
        }
    }
}