#include <stdio.h>

int main(){
    int x = 0;
    
    scanf("%i", &x);

    printf("%i\n", x);
    printf("%i nota(s) de R$ 100,00\n", x/100);
    x = x%100;
    printf("%i nota(s) de R$ 50,00\n", x/50);
    x = x%50;
    printf("%i nota(s) de R$ 20,00\n", x/20);
    x = x%20;
    printf("%i nota(s) de R$ 10,00\n", x/10);
    x = x%10;
    printf("%i nota(s) de R$ 5,00\n", x/5);
    x = x%5;
    printf("%i nota(s) de R$ 2,00\n", x/2);
    x = x%2;
    printf("%i nota(s) de R$ 1,00\n", x/1);
    
    return 0;
}
