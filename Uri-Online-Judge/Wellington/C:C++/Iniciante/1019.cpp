#include <stdio.h>

int main(){
    int n;
    
    scanf("%i", &n);
    
    printf("%i:%i:%i\n",n/3600,(n%3600)/60,(n%3600)%60);
    
    return 0;
}
