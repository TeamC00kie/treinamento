package Iniciante;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Q1010 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.00");
        int[] codigo = new int[2] ;
        int[] quantidade = new int[2];
        double[] valor = new double[2];
        double total;
        
        for (int i = 0; i < 2; i++) {
            codigo[i] = in.nextInt();
            quantidade[i] = in.nextInt();
            valor[i] = in.nextDouble();
        }

        total = quantidade[0] * valor[0] + quantidade[1] * valor[1];
        
        System.out.println("VALOR A PAGAR: R$ " + df.format(total));
    }
}