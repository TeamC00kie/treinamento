#include <stdio.h>

int main(){
    double pesoA = 3.5;
    double pesoB = 7.5;
    double a = 0;
    double b = 0;
    double media = 0;
    
    scanf("%lf", &a);
    scanf("%lf", &b);
    
    media = (a * pesoA + b * pesoB) / (pesoA + pesoB);
    
    printf("MEDIA = %.5f\n", media);
    
    return 0;
}
