#include <stdio.h>

int main(){
    double salario, salarioFinal, porcentual;
    
    scanf("%lf", &salario);
    
    if (salario <= 400) {
        porcentual = 0.15;
        salarioFinal = (salario * porcentual) + salario;
    } else if (400 < salario && salario <= 800) {
        porcentual = 0.12;
        salarioFinal = (salario * porcentual) + salario;
    } else if (800 < salario && salario <= 1200) {
        porcentual = 0.10;
        salarioFinal = (salario * porcentual) + salario;
    } else if (1200 < salario && salario <= 2000) {
        porcentual = 0.07;
        salarioFinal = (salario * porcentual) + salario;
    } else if (2000 < salario) {
        porcentual = 0.04;
        salarioFinal = (salario * porcentual) + salario;
    }
    
    char a[2] = {"%"};
    printf("Novo salario: %.2lf\n", salarioFinal);
    printf("Reajuste ganho: %.2lf\n", salarioFinal - salario);
    printf("Em percentual: %.0lf %s\n", porcentual * 100, a);
    
    return 0;
}
