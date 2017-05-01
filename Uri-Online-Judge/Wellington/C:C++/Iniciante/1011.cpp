#include <stdio.h>
#include <math.h>
#define PI 3.14159

int main(){
    double raio = 0;
    double volume = 0;
    
    scanf("%lf", &raio);
    
    //se (4/3) c++ reconhece como inteiro
    volume = (4.0/3) * PI * pow(raio,3);
    
    printf("VOLUME = %.3lf\n", volume);
    
    return 0;
}
