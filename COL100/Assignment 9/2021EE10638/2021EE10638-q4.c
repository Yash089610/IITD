#include <stdio.h> // mandatory include
int birt(int XX, int YY, int ZZZZ, int AA, int BB, int CCCC){   // function you have to implement
    if ((YY!=2 && XX!=29) && (BB>YY) || (BB==YY && AA>XX))){
        CCCC++;
    }
    if(YY==BB && BB==2 && XX==AA && AA==29)
        CCCC--;
    if(YY<=2 && XX!=29)
        CCCC--;
    if(YY>2)
        ZZZZ++;
    if(XX==29 && YY==2 && BB==3 && AA==1)
        CCCC--;
    //printf("%dh%d\n",ZZZZ,CCCC);
    int days=5;
    int result=0;
    for(int i=ZZZZ;i<CCCC;i++){
        if(i%4==0)
            days+=(366%7);
        else    
            days+=(365%7);
        if(days%7==0){
            result+=1;
            days=0;
        }
        //printf("%dh%d %d\n",days,i,result);
    }
    return result;
}

int main()                       // mandatory main function
{
    int XX, YY, ZZZZ, AA, BB, CCCC;             // variable 
    scanf("%d", &XX);           // input of Date of birth
    scanf("%d", &YY);            // input of Month of birth
    scanf("%d", &ZZZZ);           // input of Year of birth
    scanf("%d", &AA);           // input of Date of death
    scanf("%d", &BB);            // input of Month of death
    scanf("%d", &CCCC);            // input of Year of death
    //printf("%d-%d-%d and %d-%d-%d \n",XX, YY, ZZZZ, AA, BB, CCCC);
    int result = birt(XX, YY, ZZZZ, AA, BB, CCCC);  // calling function
    printf("%d",result);               // printing result
    return 0;                   // return statment
}
