#include <stdio.h>
#include <math.h>

int main(){
    double a = 0, b = 0, c = 0, r1, r2, delta;
    
    scanf("%lf", &a);
    scanf("%lf", &b);
    scanf("%lf", &c);
    
    if (a != 0 && (pow(b,2) - 4*a*c) > 0){
        delta = pow(b,2) - 4 * a * c;
        r1 = (-b + sqrt(delta)) / (2 * a);
        r2 = (-b - sqrt(delta)) / (2 * a);
        
        printf("R1 = %.5lf\n", r1);
        printf("R2 = %.5lf\n", r2);
    } else {
        printf("Impossivel calcular\n");
    }
    
    return 0;
}
