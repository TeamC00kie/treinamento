#include <stdio.h>

int main(){
    double a = 0;
    double b = 0;
    double c = 0;
    int pesoA = 2;
    int pesoB = 3;
    int pesoC = 5;
    double media = 0;
    
    scanf("%lf", &a);
    scanf("%lf", &b);
    scanf("%lf", &c);
    
    media = (a * pesoA + b * pesoB + c * pesoC) / (pesoA + pesoB + pesoC);
    
    printf("MEDIA = %.1f\n", media);
    
    return 0;
}
