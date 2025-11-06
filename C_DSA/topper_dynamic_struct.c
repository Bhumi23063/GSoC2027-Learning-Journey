#include<stdio.h>
#include<stdlib.h>

struct student{
    char name[100];
    int roll_no;
    float marks;
};

int main()
{
    int i , n, temp;
    struct student s[100];


    printf("Enter the number of studnets : ");
    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
        printf("Enter the name , roll number and the marks of the student %d : ", i+1);
        scanf("%s%d%f" ,s[i].name,&s[i].roll_no,&s[i].marks); 
    }

    for(i=0;i<n;i++)
    {
        if(s[i].marks < s[i+1].marks)
        {
            temp = s[i].marks;
            s[i].marks = s[i+1].marks;
            s[i+1].marks = temp;
        }
    }

    printf("The topper is : %f\n",s[0].marks);

}