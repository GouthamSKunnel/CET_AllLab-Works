#include<stdio.h>

float add(float x,float y)
{
float c=x+y;
return c;
}
void main()
{
float num1,num2,sum=0;
printf("enter 2 nos");
scanf("%f %f",&num1,&num2);
sum=add(num1,num2);
printf("sum of %f and %f = %.1f \n",num1,num2,sum);
}

