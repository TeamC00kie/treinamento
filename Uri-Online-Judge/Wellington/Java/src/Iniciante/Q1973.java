package Iniciante;

import java.util.Scanner;

public class Q1973 {
    
    public static void main(String[]args){
        Scanner in = new Scanner(System.in);
        
        int n, aux, roubados = 1, indo = 1;
        n = in.nextInt();
        
        int[] carneiros = new int[n];
        
        for (int i = 0; i < n; i++) {
            carneiros[i] = in.nextInt();
        }
        
        aux = 1;
        int i = 0;
        while(true){
            if(n - 1 == i){
                if(carneiros[i] > 0){
                    carneiros[i]--;
                }
                break;
            }
            if(indo == -1 && i == 0){
                if(carneiros[i] > 0){
                    carneiros[i]--;
                }
                break;
            }
            if(carneiros[i] % 2 == aux && indo == 1){
                roubados++;
            }
            if(carneiros[i] % 2 == aux){
                if(carneiros[i] > 0){
                    carneiros[i]--;
                }
            }else{
                if(carneiros[i] > 0){
                    carneiros[i]--;
                }
                aux = 1;
                indo = -1;
            }
            
            i += indo;
        }
        
        int total = 0;
        for (int j = 0; j < n; j++) {
            total += carneiros[j];
        }
        
        System.out.println(roubados + " " + total);
    }
    
}
