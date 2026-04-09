from abc import ABC, abstractmethod

class GiaCaKhongHopLe(Exception):
    def __init__(self, gia):
        self.gia = gia
        super().__init__(f"Giá cả không hợp lệ: {gia}")

class hanghoa(ABC):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.nha_sx = nha_sx
        self.gia = gia

    @property
    def ma_hang(self):
        return self._ma_hang

    @ma_hang.setter
    def ma_hang(self, value):
        self._ma_hang = value

    @property
    def ten_hang(self):
        return self._ten_hang

    @ten_hang.setter
    def ten_hang(self, value):
        self._ten_hang = value

    @property
    def nha_sx(self):
        return self._nha_sx

    @nha_sx.setter
    def nha_sx(self, value):
        self._nha_sx = value

    @property
    def gia(self):
        return self._gia

    @gia.setter
    def gia(self, gia):
        if gia < 0:
            raise GiaCaKhongHopLe(gia)
        self._gia = gia

    @abstractmethod
    def loai_hang(self):
        pass

    def hienthi(self):
        print(f" Mã hàng: {self.ma_hang}, Tên hàng: {self.ten_hang}, "
              f"Nhà sản xuất: {self.nha_sx}, Giá: {self.gia}")

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return (f" Mã hàng: {self.ma_hang}, Tên hàng: {self.ten_hang}, "
                f"Nhà sản xuất: {self.nha_sx}, Giá: {self.gia}")

    def __eq__(self, other):
        if isinstance(other, hanghoa):
            return self.ma_hang == other.ma_hang
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, hanghoa):
            return self.gia < other.gia
        return NotImplemented

    def __hash__(self):
        return hash(self.ma_hang)


class HangDienMay(hanghoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, tg_baohanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.tg_baohanh = tg_baohanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat

    def loai_hang(self):
        return "Hàng điện máy"

    def hienthi(self):
        super().hienthi()
        print(f" Thời gian bảo hành: {self.tg_baohanh}")
        print(f" Điện áp: {self.dien_ap}")
        print(f" Công suất: {self.cong_suat}")


class HangSanhSu(hanghoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyenlieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.loai_nguyenlieu = loai_nguyenlieu

    def loai_hang(self):
        return "Hàng sành sứ"

    def hienthi(self):
        super().hienthi()
        print(f" Loại nguyên liệu: {self.loai_nguyenlieu}")


class HangThucPham(hanghoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_hethan):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.ngay_sx = ngay_sx
        self.ngay_hethan = ngay_hethan

    def loai_hang(self):
        return "Hàng thực phẩm"

    def hienthi(self):
        super().hienthi()
        print(f" Ngày sản xuất: {self.ngay_sx}")
        print(f" Ngày hết hạn: {self.ngay_hethan}")


sp1 = HangDienMay("DM001", "Tu lanh Samsung", "Samsung", 10000000, "24 thang", "220V", "150W")
sp2 = HangSanhSu("NVM002", "Bo bat dia gom su Nhat Ban", "Nhat Ban", 500000, "Bo gom su")
sp3 = HangThucPham("JJ001", "Thit bo Wagyu", "Nhat Ban", 2000000, "01/04/2026", "01/05/2026")

sp1.hienthi()
print()
sp2.hienthi()
print()
sp3.hienthi()
