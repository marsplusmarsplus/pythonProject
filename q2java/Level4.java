import java.util.Scanner;
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
            System.out.print("   distance "+Math.round(distance*10.0)/10.0);
            System.out.print("  climbed "+Math.round((C-fatigue*(attempt-1))*10.0)/10.0);
            if(fatigue*(attempt-1)>C) distance=distance-S;
            else distance=distance+C-fatigue*(attempt-1)-S;
            System.out.print("   climbing "+Math.round((distance+S)*10.0)/10.0);
            System.out.println("   sliding "+Math.round(distance*10.0)/10.0);
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