import java.util.Scanner;
public class Level2b   
{  
    public static void main(String[] args) {  

        Scanner keyboard = new Scanner(System.in);
        String str=keyboard.nextLine();
        str=str.toUpperCase();
        char alphabet[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".toCharArray();
        while(!str.equals("STOP")){
            int[] freq = new int[26];
            for (int i=0;i<26;i++) 
                freq[i]=0;    
            char inputString[] = str.toCharArray();  
            for(int i = 0; i <str.length(); i++) {  
                for(int j = 0; j<26; j++)   
                    if(inputString[i] == alphabet[j]) 
                        freq[j]++;
            }
            boolean first=true;
            for (int i=0;i<26;i++)
                if(freq[i]>0){
                    if (first)
                        first=false;
                    else
                        System.out.print(" : ");
                    System.out.print(alphabet[i]+"-"+freq[i]);
                }
            System.out.println();
            System.out.println();
            str=keyboard.nextLine();
            str=str.toUpperCase();
        }
    }  
} 