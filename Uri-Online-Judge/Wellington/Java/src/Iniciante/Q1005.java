package Iniciante;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Q1005 {
    
    public static void main(String[]args){
        Scanner in = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.00000");
        double a, aPeso = 3.5, b, bPeso = 7.5, media;
        
        a = in.nextDouble();
        b = in.nextDouble();
        
        a *= aPeso;
        b *= bPeso;
        
        media = (a + b)/(aPeso + bPeso);
        
        System.out.println("MEDIA = " + df.format(media));
    }
}