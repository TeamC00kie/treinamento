package Iniciante;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Q1040 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.0");

        double n1 = in.nextDouble() * 2;
        double n2 = in.nextDouble() * 3;
        double n3 = in.nextDouble() * 4;
        double n4 = in.nextDouble();

        double media = (n1 + n2 + n3 + n4) / 10;

        System.out.println("Media: " + df.format(media));
        if (media >= 7) {
            System.out.println("Aluno aprovado.");
        } else if (media < 5) {
            System.out.println("Aluno reprovado.");
        } else {
            System.out.println("Aluno em exame.");
            double exame = in.nextDouble();
            media = (media + exame) / 2;
            System.out.println("Nota do exame: " + df.format(exame));
            if (media >= 5) {
                System.out.println("Aluno aprovado.");
            } else {
                System.out.println("Aluno reprovado.");
            }
            System.out.println("Media final: " + df.format(media));
        }
    }
}
