#include <stdio.h>
#include <math.h>
#define PI 3.14159

int main(){
    double a = 0;
    double b = 0;
    double c = 0;
    double triangulo = 0;
    double circulo = 0;
    double trapezio = 0;
    double quadrado = 0;
    double retangulo = 0;
    
    scanf("%lf", &a);
    scanf("%lf", &b);
    scanf("%lf", &c);
    
    triangulo = (a * c)/2;
    printf("TRIANGULO: %.3lf\n", triangulo);
    
    circulo = PI * pow(c,2);
    printf("CIRCULO: %.3lf\n", circulo);
    
    trapezio = (c * (a + b))/2;
    printf("TRAPEZIO: %.3lf\n", trapezio);
    
    quadrado = pow(b,2);
    printf("QUADRADO: %.3lf\n", quadrado);
    
    retangulo = a * b;
    printf("RETANGULO: %.3lf\n", retangulo);
    
    return 0;
}
