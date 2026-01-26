#include <stdio.h>

int main()
{
    int numero;
    printf("\ndammi un numero per calcolare il fattoriale: ");
    scanf("%d", &numero);
    int n=numero;
    int fattoriale=1;
    while(n > 0){
        fattoriale=fattoriale*n;
        n--;
    }
    printf("il fattoriale di %d e': %d", numero, fattoriale);
}