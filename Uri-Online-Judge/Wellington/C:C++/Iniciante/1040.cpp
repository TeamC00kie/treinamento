#include <stdio.h>

int main(){
    double n1, pesoN1 = 2, n2, pesoN2 = 3, n3, pesoN3 = 4, n4, pesoN4 = 1, media, exame;
    
    scanf("%lf", &n1);
    scanf("%lf", &n2);
    scanf("%lf", &n3);
    scanf("%lf", &n4);
    
    media = (n1 * pesoN1 + n2 * pesoN2 + n3 * pesoN3 + n4 * pesoN4) / (pesoN1 + pesoN2 + pesoN3 + pesoN4);
    
    printf("Media: %.1lf\n",  media);
    if (media < 5) {
        printf("Aluno reprovado.\n");
    } else if (media >= 7){
        printf("Aluno aprovado.\n");
    } else {
        printf("Aluno em exame.\n");
        scanf("%lf", &exame);
        printf("Nota do exame: %.1lf\n", exame);
        media = (media + exame)/2;
        if (media < 5) {
            printf("Aluno reprovado.\n");
        } else {
            printf("Aluno aprovado.\n");
        }
        printf("Media final: %.1lf\n", media);
    }
    
    return 0;
}
