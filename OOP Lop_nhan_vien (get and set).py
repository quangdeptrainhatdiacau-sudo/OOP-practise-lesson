class NhanVien:
    def __init__(self,ten_nhan_vien, luong_co_ban, he_so_luong, luong_max):
        self.ten_nhan_vien = ten_nhan_vien
        self.luong_co_ban = luong_co_ban
        self.he_so_luong = he_so_luong
        self.luong_max = luong_max
    def tinh_luong(self):
        luong = self.luong_co_ban * self.he_so_luong
        return luong 
    def inTTin(self):
        print(f"Ten nhan vien: {self.ten_nhan_vien}")
        print(f"Luong co ban: {self.luong_co_ban}")
        print(f"He so luong: {self.he_so_luong}")
        print(f"Luong max: {self.luong_max}")
    def tang_luong(self,so_tien):
        he_so_moi = self.he_so_luong + so_tien
        luong_moi = self.luong_co_ban * he_so_moi
        if luong_moi > self.luong_max:
            print("Luong moi vuot qua muc luong max. Khong the tang luong.")
            return False
        else:
            self.he_so_luong = he_so_moi
            print(f"Luong da duoc tang. He so luong moi: {self.he_so_luong}")
            return True
    def get_ten_nhan_vien(self):
        return self.ten_nhan_vien
    def set_ten_nhan_vien(self, ten_nhan_vien):
        self.ten_nhan_vien = ten_nhan_vien
    def get_luong_co_ban(self):
        return self.luong_co_ban    
    def set_luong_co_ban(self, luong_co_ban):
        self.luong_co_ban = luong_co_ban
    def get_he_so_luong(self):
        return self.he_so_luong
    def set_he_so_luong(self, he_so_luong):
         self.he_so_luong = he_so_luong
    def get_luong_max(self):
        return self.luong_max   
    def set_luong_max(self, luong_max):
         self.luong_max = luong_max
# Tạo đối tượng NhanVien
nhan_vien1 = NhanVien("Nguyen Van A", 5000000, 2.0, 20000000)
# Hiển thị thông tin nhân viên
nhan_vien1.inTTin()
# Tăng lương cho nhân viên
nhan_vien1.tang_luong(1.5)
# Hiển thị thông tin nhân viên sau khi tăng lương
nhan_vien1.inTTin()
