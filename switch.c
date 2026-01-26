#include <stdio.h>


int main()
{
    int selezione;
    printf("Menu del ristorante\n1 aragoste\n2 scampi\n3 bistecca\n4 tofu alla piastra\n");
    scanf("%d", &selezione);
    switch(selezione)
    {
        case 1:
            printf("Eccoti l'aragosta\n");
            break;
        case 2:
            printf("Eccoti gli scampi\n"); //voglio che la bistecca sia in regalo con gli scampi
            // break;
        case 33: // prevengo errore del cliente che digita 2 volte 3
        case 3:
            printf("Eccoti la bistecca\n");
            break;
        case 4:
            printf("Eccoti il tofu alla piastra\n");
            break;
        default:
            printf("Non ho capito!");
    }
    /*
    if (selezione == 1) printf("Eccoti l'aragosta\n");
    if (selezione == 2) printf("Eccoti gli scampi\n");
    if (selezione == 3) printf("Eccoti la bistecca\n");
    if (selezione == 4) printf("Eccoti il tofu\n");
    if (selezione > 4 && selezione < 1) printf("non ho capito la richiesta\n");
    */

}