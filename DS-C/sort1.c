#include<stdio.h>
main(){
	int ar[5];
	printf("Enter Array Elements.\n");
	for(int i=0;i<5;++i)
		scanf("%d",&ar[i]);

	printf("Original Array.\n");
	for(int i=0;i<5;i++)
		printf("%d\t",ar[i]);

	//for(int k=0;k<5;k++){
		for(int i=0;i<4;i++){
			for(int j=i+1;j<5;j++){
				if(ar[i]>ar[j]){
					int t=ar[j];
					ar[j]=ar[i];
					ar[i]=t;
				}
			}
		}
	//}

	printf("\nSorted Array.\n");
	for(int i=0;i<5;++i)
		printf("%d\t",ar[i]);
	printf("\n");

}
