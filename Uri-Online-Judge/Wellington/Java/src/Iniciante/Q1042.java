package Iniciante;

import java.util.Arrays;
import java.util.Scanner;

public class Q1042 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] numeros = new int[3];

        numeros[0] = in.nextInt();
        numeros[1] = in.nextInt();
        numeros[2] = in.nextInt();

        int[] ordenado = duplicar(numeros);
        Arrays.sort(ordenado);

        imprimir(ordenado);
        System.out.println("");
        imprimir(numeros);

    }

    public static void imprimir(int[] vetor) {
        for (int i = 0; i < vetor.length; i++) {
            System.out.println(vetor[i]);
        }
    }

    public static int[] duplicar(int[] vetor) {
        int[] saida = new int[vetor.length];
        for (int i = 0; i < vetor.length; i++) {
            saida[i] = vetor[i];
        }
        return saida;
    }
}
