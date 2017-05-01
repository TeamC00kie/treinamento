#include <stdio.h>

int main(){
    char nome[30];
    double salario = 0;
    double totalVendas = 0;
    double salarioTotal = 0;
    double comissao = 0.15;
    
    scanf("%s", nome);
    scanf("%lf", &salario);
    scanf("%lf", &totalVendas);
    
    salarioTotal = (totalVendas * comissao) + salario;
    
    printf("TOTAL = R$ %.2lf\n", salarioTotal);
    
    return 0;
}
