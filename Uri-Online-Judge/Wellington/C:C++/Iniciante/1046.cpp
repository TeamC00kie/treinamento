#include <stdio.h>

int main(){
	int horaInicial, horaFinal, horasJogadas;

	scanf("%i", &horaInicial);
	scanf("%i", &horaFinal);

	horasJogadas = horaFinal - horaInicial;

	if (horasJogadas < 0){
		horasJogadas = 24 + (horaFinal - horaInicial);
	}

	if (horaFinal == horaInicial){
		printf("O JOGO DUROU 24 HORA(S)\n");
	}else {
		printf("O JOGO DUROU %i HORA(S)\n", horasJogadas);
	}

	return 0;
}