#include <stdio.h>
#include <stdlib.h>

int main(){
    int a = 0;
    int b = 0;
    int c = 0;
    int maiorAB = 0;
    int maior = 0;
    
    scanf("%i", &a);
    scanf("%i", &b);
    scanf("%i", &c);
    
    maiorAB = (a + b + abs(a-b))/2;
    maior = (maiorAB + c +abs(maiorAB - c))/2;
    
    printf("%i eh o maior\n", maior);
    
    return 0;
}
