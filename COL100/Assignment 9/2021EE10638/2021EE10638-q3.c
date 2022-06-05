#include <stdio.h> // mandatory include

long long unsigned int ncr(int n,int r){
    if (r==0)
        return 1;
    if(r>n-r)
        r=n-r;
    return (n*ncr(n-1,r-1))/r;
}
int food(int x, int y, int m, int n){   // function you have to implement
    long long unsigned int result = 0;          // sample variable - you can change this according to your need
    //printf("(%d,%d) and (%d,%d) \n",x,y,m,n);
    result=ncr(x+y,x)*ncr(m+n-x-y,m-x);
    return result;                 // return statment
}

int main()                       // mandatory main function
{
    int x, y, m, n;             // variable denoting coordinate of restaurant and delivery location
    scanf("%d", &x);           // x coordinate of restaurant
    scanf("%d", &y);            // y coordinate of restaurant
    scanf("%d", &m);           // x coordinate of delivery location
    scanf("%d", &n);            // y coordinate of delivery location
    //printf("(%d,%d) and (%d,%d) \n",x,y,m,n);
    int result = food(x, y, m, n);  // calling function
    printf("%d",result);               // printing result
    return 0;                   // return statment
}
