package Iniciante;

import java.util.Scanner;

public class Q1020 {
    
    public static void main(String[]args){
        Scanner in = new Scanner(System.in);
        
        int tempo = in.nextInt();
        
        System.out.println(tempo / 365 + " ano(s)");
        System.out.println((tempo % 365) / 30 + " mes(es)");
        System.out.println((tempo % 365) % 30 + " dia(s)");
    }
    
}