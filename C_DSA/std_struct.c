#include<stdio.h>

struct student{
    char name[100];
    int roll_no;
    float marks;
};

void main()
{
    int i , n, temp;
    struct student s[100];

    printf("Enter the number of studnets : ");
    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
        printf("Enter the name , roll number and the marks of the student %d : ", i+1);
        scanf("%s %d %f" ,&s[i].name,&s[i].roll_no,&s[i].marks); 
    }

    for(i=0;i<n;i++)
    {
        printf("The details of the student %d are : \nName : %s \nRoll Number : %d \nMarks : %f\n", i+1, s[i].name, s[i].roll_no, s[i].marks);
    }
}
