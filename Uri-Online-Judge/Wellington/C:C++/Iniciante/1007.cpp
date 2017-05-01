#include <stdio.h>

int main(){
	int a = 0;
	int b = 0;
	int c = 0;
	int d = 0;
	int diferenca = 0;

	scanf("%i", &a);
    scanf("%i", &b);
    scanf("%i", &c);
    scanf("%i", &d);
    
    diferenca = a * b - c * d;
    
    printf("DIFERENCA = %i\n", diferenca);

	return 0;
}
