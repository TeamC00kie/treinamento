#include <stdio.h>

int main(){
    int entrada[3], ordenado[3];
    
    for (int i = 0; i < 3; i++) {
        scanf("%i", &entrada[i]);
        ordenado[i] = entrada[i];
    }
    
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 2; j++) {
            if (ordenado[j]>ordenado[j+1]) {
                int aux = ordenado[j];
                ordenado[j] = ordenado[j+1];
                ordenado[j+1] = aux;
            }
        }
    }
    
    for (int i = 0; i < 3; i++) {
        printf("%i\n", ordenado[i]);
    }
    printf("\n");
    
    for (int i = 0; i < 3; i++) {
        printf("%i\n", entrada[i]);
    }
    
    return 0;
}
