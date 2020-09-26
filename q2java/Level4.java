import java.util.Scanner;
import java.lang.Math;
public class Level4 {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        double D=keyboard.nextInt();
        double C=keyboard.nextInt();
        double S=keyboard.nextInt();
        double F=keyboard.nextInt();
        double fatigue=C*((F)/100);
        double attempt =0;
        double distance=0;
        boolean incomplete=true;
        while (incomplete){
            attempt++;
            System.out.println();
            System.out.print("attempt "+attempt);
            System.out.print("   distance "+distance);
            System.out.print("  climbed "+(C-fatigue*(attempt-1)));
            if(fatigue*(attempt-1)>C) distance=distance-S;
            else distance=distance+C-fatigue*(attempt-1)-S;
            System.out.print("   climbing "+(distance+S));
            System.out.println("   sliding "+distance);
            if (distance +S>D) {
                System.out.println();
                System.out.println("success");
                incomplete=false;
            }
            if (distance<0) {
                System.out.println();
                System.out.println("failure");
                incomplete=false;
            }
        }
    }
}