#include<stdio.h>
main(){
	int ar[5];
	for(int i=0;i<5;i++)
		scanf("%d",&ar[i]);

	printf("Displaying array elements\n");
	for(int i=0;i<5;i++)
		printf("%d\t",ar[i]);
}
