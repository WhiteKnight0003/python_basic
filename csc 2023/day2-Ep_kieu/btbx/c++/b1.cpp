#include<bits/stdc++.h>

int tinhtien(int soluong, int dongia){
	return soluong*dongia;
}

int main(){
	int soluong, dongia;
	std::cin>>soluong>>dongia;
	std::cout<<tinhtien(soluong,dongia);
}