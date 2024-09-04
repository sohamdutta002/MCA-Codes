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
    int t,i,j;
    //Moves in reverse order starting from an index to 0 moving the current element to its correct index.
    for(i=1;i<n;i++){
        j=i-1;
        t=arr[i];
        while(j>=0 && t<=arr[j]){
            arr[j+1]=arr[j];
            j=j-1;
        }
        arr[j+1]=t;
    }
}