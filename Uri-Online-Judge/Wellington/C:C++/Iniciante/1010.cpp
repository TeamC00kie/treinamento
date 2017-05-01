#include <stdio.h>

int main(){
    int codigo1 = 0;
    int quantidade1 = 0;
    double valor1 = 0;
    int codigo2 = 0;
    int quantidade2 = 0;
    double valor2 = 0;
    double valorTotal = 0;
    
    scanf("%i", &codigo1);
    scanf("%i", &quantidade1);
    scanf("%lf", &valor1);
    scanf("%i", &codigo2);
    scanf("%i", &quantidade2);
    scanf("%lf", &valor2);
    
    valorTotal = quantidade1 * valor1 + quantidade2 * valor2;
    
    printf("VALOR A PAGAR: R$ %.2lf\n", valorTotal);
    
    return 0;
}
