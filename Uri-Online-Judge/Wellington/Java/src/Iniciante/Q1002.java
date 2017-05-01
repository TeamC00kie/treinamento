package Iniciante;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Q1002 {
    
    public static void main(String[]args){
        //Criação do objeto in para ler do terminal
        Scanner in = new Scanner(System.in);
        //Formatação casas decimais
        DecimalFormat df = new DecimalFormat("0.0000");
        //declaração das variaveis
        double pi = 3.14159;
        double raio = in.nextDouble();
        double area = pi * Math.pow(raio, 2);
        
        System.out.println("A=" + df.format(area));
        
    }
}