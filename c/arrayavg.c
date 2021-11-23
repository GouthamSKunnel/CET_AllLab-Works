#include<stdio.h>

void main()
{
int n,sum=0;
printf("Enter the limit");
scanf("%d",&n);
int arr[n];
printf("Enter the nos\n");
for(int i=0;i<n;i++)
{
scanf("%d",&arr[i]);
sum=sum+arr[i];
}
float avg=(float)sum/n;
printf("sum = %d and average = %0.1f ",sum,avg);
}

