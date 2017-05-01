package Iniciante;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Q1008 {
    
    public static void main(String[]args){
        Scanner in = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.00");
        int numero, horas;
        double valorPorHora , salario;
        
        numero = in.nextInt();
        horas = in.nextInt();
        valorPorHora = in.nextDouble();
        
        salario = horas * valorPorHora;
        
        System.out.println("NUMBER = " + numero);
        System.out.println("SALARY = U$ " + df.format(salario));
    }
}