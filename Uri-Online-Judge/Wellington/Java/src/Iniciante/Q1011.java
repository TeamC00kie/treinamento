package Iniciante;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Q1011 {
    
    public static void main(String[]args){
        Scanner in = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.000");
        
        double volume, raio, pi = 3.14159;
        
        raio = in.nextDouble();
        
        volume = (4/3.0) * pi * Math.pow(raio, 3);
        
        System.out.println("VOLUME = " + df.format(volume));
        
    }
}
