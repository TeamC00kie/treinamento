#include <stdio.h>
#define PI 3.14159

int main(){
    double area = 0;
    double raio = 0;
    
    scanf("%lf", &raio);
    area = PI * (raio*raio);
    
    printf("A=%.4f\n", area);
    
    return 0;
}
