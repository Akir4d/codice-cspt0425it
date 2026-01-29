#include <stdio.h>

void leggivettore(int *ptr)
{
    for (int i=0;i<10;i++){
        printf("\nZona di memoria = 0x%x, Il valore di num[%d] = %d", ptr, i, *ptr);
        ptr++;
    }
}

void scrivivettore(int *ptr)
{
    for (int i=0;i<10;i++){
        printf("\ninserisci un numero: ");
        scanf("%d", ptr);
        ptr++;
    }
}

int main(){
    int num[10] = {0};
    int *n_ptr;
    n_ptr = &num[0];
    scrivivettore(n_ptr);
    leggivettore(n_ptr);
    return 0;
}