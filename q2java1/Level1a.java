import java.util.Scanner;
public class Level1a   
{  
    public static void main(String[] args) {  
        Scanner keyboard = new Scanner(System.in);
        String str=keyboard.nextLine();
        while(!str.equals("Q")){
            int[] freq = new int[str.length()];  
            int i, j; 
            String winnerIs="ONE";
            boolean winner=false;
            int oneScore=0;
            int twoScore=0;
            int ties=0;
            char rps[] = str.toCharArray();  
            char charP='P';
            char charR='R';
            char charS='S';
            for(i = 0; i <str.length(); i=i+3) {  
                if(rps[i]==rps[i+1]) 
                    ties++;
                if(rps[i]==charP && rps[i+1]==charR) 
                    oneScore++;
                if(rps[i]==charR && rps[i+1]==charS) 
                    oneScore++;
                if(rps[i]==charS && rps[i+1]==charP) 
                    oneScore++;
                if(rps[i]==charP && rps[i+1]==charS) 
                    twoScore++;
                if(rps[i]==charS && rps[i+1]==charR) 
                    twoScore++;
                if(rps[i]==charR && rps[i+1]==charP) 
                    twoScore++;
                System.out.println("round "+(i/3+1)+" score is "+oneScore+" - "+twoScore);
                if (twoScore==2 && !winner){
                    winner=true;
                    winnerIs="TWO";                
                }
                if (oneScore==2 && !winner){
                    winner=true;
                    winnerIs="ONE";                
                }
            }  
            System.out.println("WINNER IS PLAYER "+winnerIs+" --- TIES = "+ties); 
            str=keyboard.nextLine();
        }
    }  
}  
