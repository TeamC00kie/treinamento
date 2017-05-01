#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void ordenar(double array[], int tamanho){
    for (int i = 0; i < tamanho; i++) {
        for (int j = 0; j < tamanho; j++) {
            if (array[j]<array[j+1]) {
                int aux = array[j];
                array[j] = array[j+1];
                array[j+1] = aux;
            }
        }
    }
}

int main(){
    int tamanho = 3;
    double v[tamanho];
    
    for (int i = 0; i < tamanho; i++) {
        scanf("%lf", &v[i]);
    }
    
    ordenar(v, tamanho);
    
    if (v[0]>= v[1]+v[2]) {
        printf("NAO FORMA TRIANGULO\n");
    } else {
		 if (pow(v[0],2) == (pow(v[1],2) + pow(v[2],2))) {
	        printf("TRIANGULO RETANGULO\n");
	    }
	    if (pow(v[0],2) > pow(v[1],2) + pow(v[2],2)){
	        printf("TRIANGULO OBTUSANGULO\n");
	    }
	    if (pow(v[0],2) < pow(v[1],2) + pow(v[2],2)){
	        printf("TRIANGULO ACUTANGULO\n");
	    }
	    if (v[0] == v[1] && v[0] == v[2]){
	        printf("TRIANGULO EQUILATERO\n");
	    }
	    if (((v[0] == v[1] && v[0] != v[2]) || (v[0] == v[2] && v[0] != v[1])) || (v[1] == v[2] && v[1] != v[0])){
	        printf("TRIANGULO ISOSCELES\n");
	    }
	}
    
    return 0;
}
