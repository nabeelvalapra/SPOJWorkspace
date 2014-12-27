#include<cstdio>
using namespace std;
int main(){
	int n = 0;
	while(true){
		scanf("%d",&n);
		if(n == 0) break;
		else{
			int tot = 0;
			for(int i=1;i <= n;i++)	tot += i*i;
			printf("%d\n",tot);
		};
		
	}
	return 0;
}

