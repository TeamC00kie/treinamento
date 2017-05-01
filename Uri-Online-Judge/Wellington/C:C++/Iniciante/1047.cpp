#include <stdio.h>

int main(){
    int horaI, horaF, minutoI, minutoF, hora, minuto;
    
    scanf("%i %i %i %i",&horaI, &minutoI, &horaF, &minutoF);
    
    minuto = minutoF - minutoI;
    
    hora = horaF - horaI;
    
    if (hora < 0) {
        hora = 24 + (horaF - horaI);
    }
    if (minutoF == minutoI) {
        hora++;
    } else if (minuto < 0) {
        minuto += 60;
        hora -= 1;
    }
    
    if (horaF == horaI) {
        printf("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)\n");
    }else{
        printf("O JOGO DUROU %i HORA(S) E %i MINUTO(S)\n", hora, minuto);
    }
    
    return 0;
}
