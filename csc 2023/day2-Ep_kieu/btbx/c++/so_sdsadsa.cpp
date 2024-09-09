#include<bits/stdc++.h>
using namespace std;

int main(){
	for(int i=0;i<=500;i++){
		if(i<10)
			cout<<"00"<<i;
		else if(i<100)
			cout<<'0'<<i;
		else cout<<i;
		cout<<endl;
	}
}