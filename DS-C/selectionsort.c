#include<stdio.h>
void sortMin(int[],int);
void sortMax(int[],int);
main(){
    int arr[]={8,2,1,4,6,7,6};
    int n=sizeof(arr)/sizeof(arr[0]);
    
    printf("Original Array:\t");
    for(int i=0;i<n;i++)
        printf("%d\t",arr[i]);
    printf("\n");
    sortMin(arr,n);
    printf("Sorted Array Ascending:  ");
    for(int i=0;i<n;i++)
        printf("%d\t",arr[i]);
    printf("\n");
    sortMax(arr,n);
    printf("Sorted Array Descending:  ");
    for(int i=0;i<n;i++)
        printf("%d\t",arr[i]);
    printf("\n\n\n");
}
void sortMin(int arr[],int n){
    int min,i,j;
    //Finds the smallest element in each iteration and moves it backward.
    for(i=0;i<n-1;i++){
        min=i;
        for(j=i+1;j<n;j++){
            if(arr[j]<arr[min]){
                min=j;
            }
        }
        //Swap if current element is not same as minimum element.
        if(i!=min){
            int t=arr[i];
            arr[i]=arr[min];
            arr[min]=t;
        }
    }
}
void sortMax(int arr[],int n){
    int i,j,max;
    for(i=0;i<n-1;i++){
        max=i;
        for(j=i+1;j<n;j++){
            if(arr[j]>arr[max])
                max=j;
        }
        if(i!=max){
            int t=arr[max];
            arr[max]=arr[i];
            arr[i]=t;
        }
    }
}