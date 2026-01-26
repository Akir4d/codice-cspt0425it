#include <stdio.h>
/*
Condizione if
*/

int main()
{
    int numeratore;
    int denominatore;
    float divisione;

    printf("\nDammi il numeratore: ");
    scanf("%d", &numeratore);

    printf("\nDammi il denominatore: ");
    scanf("%d", &denominatore);

    if (denominatore != 0){
        divisione = (float)numeratore/(float)denominatore;
        printf("\n%d/%d=%f", numeratore, denominatore, divisione);
    } else {
        printf("il denominatore non puo' essere 0");
    }
    return 0;
}