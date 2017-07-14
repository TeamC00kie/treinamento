package Iniciante;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Q1043 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.0");
        double a = in.nextDouble(), b = in.nextDouble(), c = in.nextDouble();

        if (Math.abs(b - c) < a && a < b + c && Math.abs(a - c) < b && b < a + c && Math.abs(a - b) < c && c < a + b) {
            System.out.println("Perimetro = " + df.format(a + b + c));
        } else {
            System.out.println("Area = " + df.format((c * (a + b)) / 2));
        }

    }
}
