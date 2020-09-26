import java.util.Scanner;
import java.lang.Math;
public class Level0 {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        double ic =0;
        double bc =0;
        double b=0;
        System.out.print("Enter the amount of collector current (in Amperes): ");
        ic = keyboard.nextDouble();
        System.out.println();
        System.out.print("Enter the amount of base current (in Amperes): ");
        bc = keyboard.nextDouble();
        System.out.println();
        b = ic/bc;
        System.out.println("The transistor current gain is " + b);
    }
}