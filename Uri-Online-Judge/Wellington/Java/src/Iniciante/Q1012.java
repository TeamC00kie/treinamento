package Iniciante;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Q1012 {

    public static void main(String[]args){
        Scanner in = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.000");
        
        double a, b, c, triangulo, circulo, trapezio, quadrado, retangulo, pi = 3.14159;
        a = in.nextDouble();
        b = in.nextDouble();
        c = in.nextDouble();
        
        triangulo = (a * c) / 2;
        System.out.println("TRIANGULO: " + df.format(triangulo));
        
        circulo = pi * Math.pow(c, 2);
        System.out.println("CIRCULO: " + df.format(circulo));
        
        trapezio = (c * (a + b)) / 2;
        System.out.println("TRAPEZIO: " + df.format(trapezio));
        
        quadrado = Math.pow(b, 2);
        System.out.println("QUADRADO: " + df.format(quadrado));
        
        retangulo = a * b;
        System.out.println("RETANGULO: " + df.format(retangulo));
    }
}