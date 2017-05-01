#include <stdio.h>

int main(){
    double numeros[6];
    int cont;
    
    for (int i = 0; i < 6; i++) {
        scanf("%lf", &numeros[i]);
        if (numeros[i] > 0 ) {
            cont++;
        }
    }
    
    printf("%i valores positivos\n", cont);
    
    return 0;
}
