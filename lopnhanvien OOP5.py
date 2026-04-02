LUONG_CO_BAN = 15000000
class nhan_vien:
    def __init__(self,ho_ten,nam_sinh,gioi_tinh,dia_chi,he_so_luong,luong_toi_da):
        self.ho_ten= ho_ten
        self.nam_sinh= nam_sinh
        self.gioi_tinh= gioi_tinh
        self.dia_chi= dia_chi
        self.he_so_luong= he_so_luong if he_so_luong >0 else 1.0
        self.luong_toi_da= luong_toi_da
    def tinh_luong(self):
        luong= self.he_so_luong * LUONG_CO_BAN
        if luong > self.luong_toi_da:
            return self.luong_toi_da
        else:
            return luong
    def hienthi(self): 
        print("=====Thong tin nhan vien=====")  
        print(f"Ho ten nhan vien: {self.ho_ten}")
        print(f"Nam sinh: {self.nam_sinh}")
        print(f"Gioi tinh: {self.gioi_tinh}")
        print(f"Dia chi: {self.dia_chi}")
        print(f"Luong: {self.tinh_luong()} VND")
class cong_tac_vien(nhan_vien):
    hd_hop_le= ["3 thang","6 thang","1 nam"]  
    def __init__(self,ho_ten,nam_sinh,gioi_tinh,dia_chi,he_so_luong,luong_toi_da,thoi_han_hop_dong,phu_cap_lao_dong):
        super().__init__(ho_ten,nam_sinh,gioi_tinh,dia_chi,he_so_luong,luong_toi_da)
        self.thoi_han_hop_dong= thoi_han_hop_dong
        self.phu_cap_lao_dong= phu_cap_lao_dong
        if self.thoi_han_hop_dong not in cong_tac_vien.hd_hop_le:
            raise ValueError("Thoi han hop dong khong hop le. Vui long chon 3 thang, 6 thang hoac 1 nam.")
    def tinhluong(self):
        luong= super().tinh_luong()+self.phu_cap_lao_dong
    def hienthi(self):
        super().hienthi()    
        print("=====Thong tin cong tac vien=====")
        print(f"Thoi han hop dong: {self.thoi_han_hop_dong}")
        print(f"Phu cap lao dong: {self.phu_cap_lao_dong} VND")
class nhan_vien_chinh_thuc(nhan_vien):
    def __init__(self,ho_ten,nam_sinh,gioi_tinh,dia_chi,he_so_luong,luong_toi_da,vi_tri_cong_viec):
        super().__init__(ho_ten,nam_sinh,gioi_tinh,dia_chi,he_so_luong,luong_toi_da)
        self.vi_tri_cong_viec= vi_tri_cong_viec
    def tinh_luong(self):
        super().tinh_luong()
    def hienthi(self):
        super().hienthi()
        print("=====Thong tin nhan vien chinh thuc======")
        print(f"vi tri cong viec: {self.vi_tri_cong_viec}")    
class truong_phong(nhan_vien):
    def __init__(self,ho_ten,nam_sinh,gioi_tinh,dia_chi,he_so_luong,luong_toi_da,ngay_bat_dau_quan_ly,phu_cap_quan_ly):
        super().__init__(ho_ten,nam_sinh,gioi_tinh,dia_chi,he_so_luong,luong_toi_da)
        self.ngay_bat_dau_quan_ly= ngay_bat_dau_quan_ly
        self.phu_cap_quan_ly= phu_cap_quan_ly
    def tinh_luong(self):
        luong= super().tinh_luong()+self.phu_cap_quan_ly
    def hienthi(self):
        super().hienthi()    
        print("=====Thong tin truong phong=====")
        print(f"Ngay bat dau quan ly: {self.ngay_bat_dau_quan_ly}")
        print(f"Phu cap quan ly: {self.phu_cap_quan_ly} VND")
ctv= cong_tac_vien("Đỗ Đinh Đạt",1990,"Nam","123 Đông Anh",1.5,20000000,"6 thang",5000000)
ctv.hienthi()        
nvc= nhan_vien_chinh_thuc("Trà My",1985,"Nu","456 Le Loi",2.0,25000000,"Giam doc")
nvc.hienthi()
tp= truong_phong("Phạm Văn Minh",1980,"Nam","789 Tran Hung Dao",2.5,30000000,"2020-04-03",10000000)
tp.hienthi()
