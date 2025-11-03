#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n, i;
    float sum = 0, avg;

    printf("Enyter the number of subjects : ");
    scanf("%d",&n);

    int *arr = (float*) malloc (n * sizeof(float));
    if (arr == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    printf("Enter the marks : ");
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }

    for(i=0;i<n;i++)
    {
        printf("%d\t",arr[i]);
    }

    sum = 0;

    for(i=0;i<n;i++)
    {
        sum = sum + arr[i];
    }

    avg = sum/n;

    printf("\nThe average of the marks is : %f\n",avg);

    free(arr);
}