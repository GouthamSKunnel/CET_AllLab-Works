#include<stdio.h>

void main()
{
int a,factorial=1;
printf("enter the number ");
scanf("%d",&a);
int b=a;
while(a>=1)
{
factorial=factorial*a;
a--;
}
printf("factorial of %d = %d \n",b,factorial);
}
