#include<stdio.h>
#include<string.h>
void Merge(int[],int,int,int);
void Sort(int[],int,int);
int n;
main(){
    int arr[]={8,2,1,4,6,7,6};
    n=sizeof(arr)/sizeof(arr[0]);
    
    printf("Original Array:\t");
    for(int i=0;i<n;i++)
        printf("%d\t",arr[i]);
    printf("\n");
    Sort(arr,0,n-1);
    printf("Sorted Array:\t");
    for(int i=0;i<n;i++)
        printf("%d\t",arr[i]);
    printf("\n\n\n");
}
void Sort(int arr[],int beg,int end){
    if(beg<end){
        //Works by dividing and merging the array
        int mid=(beg+end)/2;
        Sort(arr,beg,mid);
        Sort(arr,mid+1,end);
        Merge(arr,beg,mid,end);
    }
}
void Merge(int arr[],int beg,int mid,int end){
    int temp[end-beg+1];
    memset(temp,-1,sizeof(temp));
    int i=beg,j=mid+1,index=0;
    //Divides the array into two parts
    //Sorts the array and stores into temp array
    while(i<=mid&&j<=end){
        if(arr[i]<arr[j]){
            temp[index]=arr[i];
            i++;
        }
        else{
            temp[index]=arr[j];
            j++;
        }
        index++;
    }
    //Copy remaining elements from right subarray if any.
    while(j<=end){
        temp[index]=arr[j];
        j++;
        index++;
    }
    //Copy remaining elements from left subarray if any.
    while (i <= mid){
        temp[index] = arr[i];
        i++;
        index++;
    }
    //Copy the temp array to original array.
    int k=0;
    for(i=beg;i<=end;i++){
        arr[i]=temp[k++];
    }
}
