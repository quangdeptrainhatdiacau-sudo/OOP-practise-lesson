class hanghoa:
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.nha_sx = nha_sx
        self.gia = gia
    def getMahang(self):
        return self.ma_hang
    def getTenhang(self):
        return self.ten_hang
    def getNhasx(self):
        return self.nha_sx
    def getGia(self):
        return self.gia
    def setMahang(self, ma_hang):
        self.ma_hang = ma_hang
    def setTenhang(self, ten_hang):
        self.ten_hang = ten_hang
    def setNhasx(self, nha_sx):
        self.nha_sx = nha_sx
    def setGia(self, gia):
        self.gia = gia
    def Hienthi(self):
        print(f" Mã hàng: {self.ma_hang}, Tên hàng: {self.ten_hang}, Nhà sản xuất: {self.nha_sx}, Giá: {self.gia}")    
class HangDienMay(hanghoa):
    def __init__(self, ma_hang, ten_hang, nha_sx,gia,tg_baohanh,dien_ap,cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)   
        self.tg_baohanh = tg_baohanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat
    def hienthi(self):
        super().Hienthi()
        print(f" Thời gian bảo hành: {self.tg_baohanh}")
        print(f" Điện áp: {self.dien_ap}")
        print(f" Công suất: {self.cong_suat}")
class HangSanhSu(hanghoa):
    def __init__(self, ma_hang, ten_hang, nha_sx,gia,loai_nguyenlieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)   
        self.loai_nguyenlieu = loai_nguyenlieu
class HangThucPham(hanghoa):
    def __init__(self,ma_hang, ten_hang, nha_sx,gia,ngay_sx,ngay_hethan):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.ngay_sx= ngay_sx
        self.ngay_hethan= ngay_hethan
    def hienthi(self):
        super().Hienthi()
        print(f" Ngày sản xuất: {self.ngay_sx}")
        print(f" Ngày hết hạn: {self.ngay_hethan}")

dm=HangDienMay("DM003","Dieu hoa LG","LG",12000000,"24 thang","220V","5HP")                    
dm.Hienthi()
print()
ss=HangSanhSu("NVM002","Bo bat dia gom su Nhat Ban","Nhat Ban", 500000,"Bo gom su")
ss.Hienthi()
print()
tp=HangThucPham("JJ001","Thit bo Wagyu","Nhat Ban", 2000000, "01/04/2026", "01/05/2026")
tp.Hienthi()
print()
