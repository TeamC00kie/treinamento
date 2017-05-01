package Iniciante;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Q1017 {
    
    public static void main(String[]args){
        Scanner in = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.000");
        
        int tempo, velocidade;
        double distancia, litros;
        
        tempo = in.nextInt();
        velocidade = in.nextInt();
        
        distancia = tempo * velocidade;
        litros = distancia / 12;
        
        System.out.println(df.format(litros));
    }
    
}
