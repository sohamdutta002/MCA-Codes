#include<stdio.h>
int Search(int[],int,int);
main(){
    int arr[]={8,2,1,4,6,7,6};
    int n=sizeof(arr)/sizeof(arr[0]);
    
    printf("Original Array:\t");
    for(int i=0;i<n;i++)
        printf("%d\t",arr[i]);
    printf("\n");
    int k=2;
    int t=Search(arr,n,k);
    if(t==-1)
        printf("Not Present in Current Array");
    else    
        printf("\tValue %d found in Current Array at: %d",k,t);
    printf("\n\n\n");
}

int Search(int arr[],int n,int k){
    int i;
    //Checked with each element in the array.
    for(i=0;i<n;i++)
        if(arr[i]==k)
            return i;
    return -1;
}
