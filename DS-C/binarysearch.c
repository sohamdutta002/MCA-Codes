#include<stdio.h>
int Search(int[],int,int);
main(){
    int arr[]={1,5,8,9,15,21,56,89,100,150,151,152,153,478,499};
    int n=sizeof(arr)/sizeof(arr[0]);
    
    printf("Original Array:\t");
    for(int i=0;i<n;i++)
        printf("%d\t",arr[i]);
    printf("\n");
    int k=211;
    int t=Search(arr,n,k);
    if(t==-1)
        printf("Not Present in Current Array");
    else    
        printf("\tValue %d found in Current Array at: %d",k,t+1);
    printf("\n\n\n");
}

int Search(int arr[],int n,int k){
    int mid,beg=0,end=n-1;
    while(beg<=end){
        //mid is the actual middle
        mid=(beg+end)/2;
        if(arr[mid]==k)
            return mid;
        else if(arr[mid]>k)
            end=mid-1;
        else
            beg=mid+1;
    }
    return -1;
}