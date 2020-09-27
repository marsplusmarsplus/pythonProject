import java.util.Scanner;
public class Level3 {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        String[] names= new String[4];
        String best;
        double maxname=0;
        double[] intArray = new double[4];
        double[] intArray2 = new double[4];
        double ic =0;
        for (int i = 0; i < 4; i++) {
            names[i]=keyboard.next();
            intArray[i]=keyboard.nextDouble();
            intArray2[i]=keyboard.nextDouble();
        }
        best=names[0];
        for (int i = 0; i < 4; i++) {
            System.out.println();
            System.out.print(names[i]+" - ");
            ic=intArray2[i]/intArray[i];
            System.out.println(Math.round(ic*10000.0)/100.0);
            if (ic>maxname){
                best=names[i];
                maxname=ic;
            }

        }
        System.out.println();
        System.out.println("best player is " + best);
    }
}