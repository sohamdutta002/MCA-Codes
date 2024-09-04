#include<stdio.h>
main(){
	printf("Enter the number of terms.\n");
	int n;
	scanf("%d",&n);

	int t1=0,t2=1,next;
	printf("%d\t%d\t",t1,t2);
	for(int i=1;i<=n;i++){
		next=t1+t2;
		printf("%d\t",next);
		t1=t2;
		t2=next;
	}
	printf("\n");
}
