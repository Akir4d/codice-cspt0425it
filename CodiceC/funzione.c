#include <stdio.h>

int somma(int a, int b)
{
    int c = 0;
    // printf("\n Lo so e' stupido che io qui debba sommare %d e %d", a, b);
    c = a + b;
    return c;
}

int main()
{
    int sum = somma(5, 10);
    printf("\n5+10=%d", sum);
    printf("\n30+12=%d", somma(30, 12));
    return 0;
}
