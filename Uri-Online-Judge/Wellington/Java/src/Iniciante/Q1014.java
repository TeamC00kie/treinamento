package Iniciante;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Q1014 {
    
    public static void main(String[]args){
        Scanner in = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.000");
        int distancia;
        double combustivel, consumoMedio;
        
        distancia = in.nextInt();
        combustivel = in.nextDouble();
        
        consumoMedio = distancia / combustivel;
        
        System.out.println(df.format(consumoMedio) + " km/l");
    }
}