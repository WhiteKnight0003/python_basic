#include<bits/stdc++.h>
const double PI = 3.14159265358979323846;

class hinhtron{
private:
	float r;
public:
	hinhtron(){};
	hinhtron(int r){
		this->r =r;
	}
	float getR(){
		return r;
	}
	void setR(float R){
		r = R;
	}
	float chuvi(){
		return 2*PI*r;
	}

	float dientich(){
		return r*r*PI;
	}
};

int main(){

	int r;
	std::cin>>r;
		hinhtron a(r);
	std::cout<<a.chuvi() <<"    ---- "<<a.dientich()<<std::endl;
}