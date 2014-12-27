#include<stdio.h>
int main(){
	int t;
	scanf("%d", &t);
	for(int i=0;i<t;i++){
		char str[100000];
		scanf("%s",str);
		int node = 1;
		int j = 0;
		int left;
		while(str[j] != '\0'){
			if(node%2==1){
				left = node*2;	
			}else{
				left = (node*2)-1;
			}
			if(str[j] == 'l'){
				node = left;
			}else{
				node = left + 2;
			}
			j++;
		}
		printf("%d\n",node);
	}		
	
	return 0;
	
}
