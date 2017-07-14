package Iniciante;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Q1038 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.00");

        int codigo = in.nextInt();
        int quantidade = in.nextInt();
        double total = 0;
        if (codigo == 1) {
            total = quantidade * 4.00;
        } else if (codigo == 2) {
            total = quantidade * 4.50;
        } else if (codigo == 3) {
            total = quantidade * 5.00;
        } else if (codigo == 4) {
            total = quantidade * 2.00;
        } else if (codigo == 5) {
            total = quantidade * 1.50;
        }
        System.out.println("Total: R$ " + df.format(total));
    }
}
