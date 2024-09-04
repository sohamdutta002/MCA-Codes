#include<stdio.h>
void Sort(int[],int);
main(){
    int arr[]={8,2,1,4,6,7,6};
    int n=sizeof(arr)/sizeof(arr[0]);
    
    printf("Original Array:\t");
    for(int i=0;i<n;i++)
        printf("%d\t",arr[i]);
    printf("\n");
    Sort(arr,n);
    printf("Sorted Array:\t");
    for(int i=0;i<n;i++)
        printf("%d\t",arr[i]);
    printf("\n\n\n");
}
void Sort(int arr[],int n){
    int i,j,c=0;
    //Checks next indexes and swap each other if not in right order.
    for(i=0;i<n-1;i++){
        //If no swapping occurs in an entire run, then stop executing.
        c=0;
        for(j=0;j<n-i-1;j++){
            if(arr[j]>arr[j+1]){
                int t=arr[j+1];
                arr[j+1]=arr[j];
                arr[j]=t;
                c=1;
            }
        }
        if(c==0)
            break;
    }
}