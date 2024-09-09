#include<bits/stdc++.h>

class gui_tiet_kiem{
private:
	float lai_xuat;
	float so_tien_gui;
	int so_thang;
public:
	gui_tiet_kiem(){};
	gui_tiet_kiem(float lai_xuat,float so_tien_gui,int so_thang){
		this->lai_xuat = lai_xuat;
		this->so_tien_gui = so_tien_gui;
		this->so_thang = so_thang;
	};

	float tienlai(){
		return so_tien_gui*so_thang*(lai_xuat/100)/12;
	}

	float tong_tien(){
		return so_tien_gui+tienlai();
	}
};

int main(){
	int so_thang;
	float so_tien_gui, lai_xuat;

	std::cin>>lai_xuat>>so_tien_gui>>so_thang;
	gui_tiet_kiem a(lai_xuat, so_tien_gui, so_thang);
	std::cout<<"Tiền lãi : "<<a.tienlai()<<"\nTổng tiền thu được : "<<a.tong_tien()<<"\n";
}