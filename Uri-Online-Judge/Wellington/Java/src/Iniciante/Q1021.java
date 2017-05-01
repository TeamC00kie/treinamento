package Iniciante;

import java.util.Scanner;

public class Q1021 {
    
    public static void main(String[]args){
        Scanner in = new Scanner(System.in);
        
        int notas, moedas;
        double total = in.nextDouble();
        
        notas = (int) total;
        moedas = (int) ((total - notas) * 100);
        
        System.out.println("NOTAS:");
        System.out.println(notas / 100 + " nota(s) de R$ 100.00");
        notas %= 100;
        System.out.println(notas / 50 + " nota(s) de R$ 50.00");
        notas %= 50;
        System.out.println(notas / 20 + " nota(s) de R$ 20.00");
        notas %= 20;
        System.out.println(notas / 10 + " nota(s) de R$ 10.00");
        notas %= 10;
        System.out.println(notas / 5 + " nota(s) de R$ 5.00");
        notas %= 5;
        System.out.println(notas / 2 + " nota(s) de R$ 2.00");
        notas %= 2;
        System.out.println("MOEDAS:");
        System.out.println(notas + " moeda(s) de R$ 1.00"); //Apesar de ser uma moeda ele ainda não é um número fracionado
        System.out.println(moedas / 50 + " moeda(s) de R$ 0.50");
        moedas %= 50;
        System.out.println(moedas / 25 + " moeda(s) de R$ 0.25");
        moedas %= 25;
        System.out.println(moedas / 10 + " moeda(s) de R$ 0.10");
        moedas %= 10;
        System.out.println(moedas / 5 + " moeda(s) de R$ 0.05");
        moedas %= 5;
        System.out.println(moedas + " moeda(s) de R$ 0.01");
    }
    
}