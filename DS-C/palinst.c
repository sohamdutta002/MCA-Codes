#include<stdio.h>
#include<string.h>

int main(){
	char str[50];
	printf("Enter string:\t");
	scanf("%s",str);
	int len=strlen(str);

	for(int i=0;i<len;i++){
		if(str[i]!=str[len-i-1]){
			printf("Not Palindrome.\n");
			return -1;
		}
	}

	printf("Palindrome String\n");
	return 0;

}

