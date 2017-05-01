package Iniciante;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Q1009 {
    
    public static void main(String[]args){
        Scanner in = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.00");
        
        String nome;
        double salario, vendas, comissao = 0.15;
        
        nome = in.nextLine();
        salario = in.nextDouble();
        vendas = in.nextDouble();
        
        salario += vendas * comissao;
        
        System.out.println("TOTAL = R$ " + df.format(salario));
        
        
    }
}
