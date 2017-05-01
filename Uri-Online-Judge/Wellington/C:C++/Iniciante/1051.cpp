#include <stdio.h>

int main(){
    double salario, imposto;
    
    scanf("%lf", &salario);
    
    if (salario <= 2000) {
        printf("Isento\n");
    } else {
        double imposto8 = salario - 2000;
        if (imposto8 <= 1000) {
            imposto = imposto8 * 0.08;
        } else {
            double imposto18 = imposto8 - 1000;
            imposto8 = 1000 * 0.08;
            if (imposto18 <= 1500) {
                imposto18 = imposto18 * 0.18;
                imposto = imposto8 + imposto18;
            } else {
                double imposto28 = (imposto18 - 1500) * 0.28;
                imposto18 = 1500 * 0.18;
                imposto = imposto8 + imposto18 + imposto28;
            }
        }
        
        printf("R$ %.2lf\n", imposto);
    }
    
    
    return 0;
}
