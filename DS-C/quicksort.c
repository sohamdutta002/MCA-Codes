#include<stdio.h>
#include<string.h>
int Partition(int[],int,int);
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
        //Partition array by choosing the correct index i.e loc for arr[0]
        int loc=Partition(arr,beg,end);
        //Sort the array before and after the loc
        Sort(arr,beg,loc-1);
        Sort(arr,loc+1,end);
    }
}
int Partition(int arr[],int beg,int end){
    int left=beg,right=end,flag=0,loc=beg;
    //Repeat loop until correct index found
    //loc!=right or left
    while(flag==0){
        //Find the element smaller than arr[loc] from right
        //If found swap and move loc to right else stop loop.
        while(arr[loc]<=arr[right]&&loc!=right)
            right--;
        if(loc==right)
            flag=1;
        else if(arr[loc]>arr[right]){
            int t=arr[loc];
            arr[loc]=arr[right];
            arr[right]=t;  
            loc=right;
        }
        //Find element greater than arr[loc] from left
        //If found swap and make loc=left else stop. 
        if(flag==0){
            while(arr[loc]>=arr[left]&&loc!=left)
                left++;
            if(loc==left)
                flag=1;
            else if(arr[loc]<arr[left]){
                int t=arr[loc];
                arr[loc]=arr[left];
                arr[left]=t;
                loc=left;
            }
        }
    }
    return loc;
}