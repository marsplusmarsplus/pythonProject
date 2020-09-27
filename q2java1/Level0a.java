import java.util.Scanner;
public class Level0a {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        double ic =0;
        double bc =0;
        double b=0;
        double bb;
        System.out.print("Enter the amount of collector current (in Amperes): ");
        ic = keyboard.nextDouble();
        System.out.println();
        while(ic!=0){
            System.out.print("Enter the amount of base current (in Amperes): ");
            bc = keyboard.nextDouble();
            System.out.println();
            b=ic/bc;
            System.out.println("The transistor current gain is " + Math.round(b*100.0)/100.0);
            System.out.println();
            System.out.print("Enter the amount of collector current (in Amperes): ");
            ic = keyboard.nextDouble();
            System.out.println();
        }
        System.out.println("end");
    }
}