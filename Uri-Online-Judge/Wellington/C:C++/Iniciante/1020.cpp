#include <stdio.h>

int main(){
    int idade;
    
    scanf("%i", &idade);
    
    printf("%i ano(s)\n", idade/365);
    printf("%i mes(es)\n", (idade%365)/30);
    printf("%i dia(s)\n", (idade%365)%30);
    
    return 0;
}
