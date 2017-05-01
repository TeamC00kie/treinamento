#include <stdio.h>
#include <stdlib.h>
#include <cmath>

int main(){
    double a, b, c;
    scanf("%lf", &a);
    scanf("%lf", &b);
    scanf("%lf", &c);
    
    if (std::abs(b-c) < a && a < b+c &&
        std::abs(a-c) < b && b < a+c &&
        std::abs(a-b) < c && c < a+b) {
        printf("Perimetro = %.1lf\n", a+b+c);
    } else {
        printf("Area = %.1lf\n", (c * (a+b))/2);
    }
    
    return 0;
}
