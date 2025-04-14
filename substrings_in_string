#include <stdio.h>
#include<string.h>
#include<stdlib.h>
int main()
{
    int d = 0;
    char str[100];
    printf("enter the string : ");
    scanf("%s",str);
    for(int i = 0;str[i]!='\0';i++)
    {
        // finding palindrome of substring;
        int k = 0;
        char check[100]={'\0'};
        for(int j = i;str[j]!='\0';j++)
        {
            check[k] = str[j];
            check[k+1] = '\0';
            if(strlen(check)!=1)
            {
                for(int l = 0;l<strlen(check)/2;l++)
                {
                    if(check[l]!=check[strlen(check)-l-1])
                    {
                        d = 1;
                        break;
                    }
                }
                // if it is a palindrome;
                if(d==0)
                {
                    printf("%s\n",check);
                }
                // if it's not a palindrome;
                else
                {
                    d=0;
                }
            }
            k = k+1;
        }   
    }
    return 0;
}
