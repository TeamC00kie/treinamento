#include <stdio.h>

int main(){
    int horas, kmph;
    double litros;
    
    scanf("%i", &horas);
    scanf("%i", &kmph);
    
    litros = (horas * kmph) / 12.0;
    
    printf("%.3lf\n", litros);
    
    return 0;
}
