package Iniciante;

import java.util.Scanner;

public class Q1013 {
    
    public static void main(String[]args){
        Scanner in = new Scanner(System.in);
        int a, b, c, maiorAB, maior;
        
        a = in.nextInt();
        b = in.nextInt();
        c = in.nextInt();
        
        maiorAB = (a + b + Math.abs(a - b)) / 2;
        maior = (maiorAB + c + Math.abs(maiorAB - c)) / 2;
        
        System.out.println(maior + " eh o maior");
        
    }
}