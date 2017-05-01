package Iniciante;

import java.util.Scanner;

public class Q1019 {
    
    public static void main(String[]args){
        Scanner in = new Scanner(System.in);
        
        int tempo = in.nextInt();
        
        System.out.println(tempo / 3600 + ":" + (tempo % 3600) / 60 + ":" + (tempo % 3600) % 60);
    }
    
}