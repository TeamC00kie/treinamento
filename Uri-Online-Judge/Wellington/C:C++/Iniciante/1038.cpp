#include <stdio.h>

int main(){
    double lanche[5] = {4.00, 4.50, 5.00, 2.00, 1.50};
    int codigo, quantidade;
    double total;
    
    scanf("%i", &codigo);
    scanf("%i", &quantidade);
    
    total = quantidade * lanche[codigo-1];
    
    printf("Total: R$ %.2lf\n", total);
    
    return 0;
}
