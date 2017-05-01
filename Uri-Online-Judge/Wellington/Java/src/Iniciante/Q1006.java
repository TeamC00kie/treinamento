package Iniciante;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Q1006 {
    
    public static void main(String[]args){
        Scanner in = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.0");
        
        double a, pesoA = 2, b, pesoB = 3, c, pesoC = 5, media;
        
        a = in.nextDouble();
        b = in.nextDouble();
        c = in.nextDouble();
        
        a *= pesoA;
        b *= pesoB;
        c *= pesoC;
        
        media = (a + b + c) / (pesoA + pesoB + pesoC);
        
        System.out.println("MEDIA = " + df.format(media));
    }
}
