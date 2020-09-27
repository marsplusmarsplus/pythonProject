public class Level2   
{  
    public static void main(String[] args) {  
        String str = "And this one only has one.";  
        str=str.toUpperCase();
        int[] freq = new int[str.length()];  
        int i, j, k;  
        char inputString[] = str.toCharArray();  
        for(i = 0; i <str.length(); i++) {  
            freq[i] = 1;  
            for(j = i+1; j <str.length(); j++) {  
                if(inputString[i] == inputString[j]) {  
                    freq[i]++;  
                    inputString[j] = '_';  
                    for (k=0;k<str.length();k++) System.out.print(inputString[k]);
                    System.out.println();
                }  
            }  
        }  
        for(i = 0; i <freq.length; i++) 
            if(inputString[i] != ' ' && inputString[i]<='Z' && inputString[i]>='A')  {
                if(i>0) System.out.print(" : ");
                System.out.print(inputString[i] + "-" + freq[i]);
            }
    }  
} 