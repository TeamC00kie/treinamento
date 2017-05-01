#include <stdio.h>

int main(){
    int numero = 0;
    int horas = 0;
    double salarioPorHora = 0;
    double salarioTotal = 0;
    
    scanf("%i", &numero);
    scanf("%i", &horas);
    scanf("%lf", &salarioPorHora);
    
    salarioTotal = horas * salarioPorHora;
    
    printf("NUMBER = %i\n", numero);
    printf("SALARY = U$ %.2lf\n", salarioTotal);
    
    return 0;
}
