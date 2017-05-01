#include <stdio.h>
#include <stdlib.h>

int main(){
    int km = 0;
    double combustivel = 0;
    double consumo = 0;
    
    scanf("%i", &km);
    scanf("%lf", &combustivel);
    
    consumo = km / combustivel;
    
    printf("%.3lf km/l\n", consumo);
    
    return 0;
}
