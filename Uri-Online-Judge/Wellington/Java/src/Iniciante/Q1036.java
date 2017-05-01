package Iniciante;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Q1036 {

    public static void main(String[]args){
        Scanner in = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.00000");
        double a,b,c,r1,r2,delta;
        
        a = in.nextDouble();
        b = in.nextDouble();
        c = in.nextDouble();
        
        delta = Math.pow(b,2) - 4*a*c;
        
        if (a != 0 && delta > 0) {
            r1 = (-b + Math.sqrt(delta)) / (2 * a);
            r2 = (-b - Math.sqrt(delta)) / (2 * a);
            
            System.out.println("R1 = " + df.format(r1));
            System.out.println("R2 = " + df.format(r2));
        } else {
            System.out.println("Impossivel calcular");
        }
    }
    
}