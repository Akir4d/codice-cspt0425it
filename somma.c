#include <stdio.h>

int main(){
    int primo_numero;
    int secondo_numero;
    int somma;

    printf("\nScrivi il primo numero: ");
    scanf("%d", &primo_numero);

    printf("\nScrivi secondo numero: ");
    scanf("%d", &secondo_numero);

    somma = primo_numero + secondo_numero;
    printf("\nSomma dei due numeri e': %d indirizzo di memoria di somma 0x%x", somma, &somma);
    printf("\nprimo - secondo=%d", primo_numero - secondo_numero);
    printf("\nprimo * secondo=%d", primo_numero * secondo_numero);
    printf("\nprimo / secondo=%d", primo_numero / secondo_numero);
    printf("\nprimo m secondo=%d", primo_numero % secondo_numero);
    return 0;
}