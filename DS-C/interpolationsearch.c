#include<stdio.h>
int Search(int[],int,int);
main(){
    int arr[]={1,5,8,9,15,21,56,89,100,150,151,152,153,478,499};
    int n=sizeof(arr)/sizeof(arr[0]);
    
    printf("Original Array:\t");
    for(int i=0;i<n;i++)
        printf("%d\t",arr[i]);
    printf("\n");
    int k=478;
    int t=Search(arr,n,k);
    if(t!=-1)    
        printf("\tValue %d found in Current Array at: %d",k,t+1);
    else
        printf("Not Present in Current Array");
    printf("\n\n\n");
}

int Search(int arr[],int n,int k){
    int mid,low=0,high=n-1,pos=-1;
    while(low<=high){
        //mid is found using this formula as it interpolates where the value can be in the array
        mid=low+(high-low)*(k-arr[low])/(arr[high]-arr[low]);
        if(arr[mid]==k){
            pos=mid;
            break;
        }
        else if(arr[mid]>k)
            high=mid-1;
        else
            low=mid+1;
    }
    return pos;
}