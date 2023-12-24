def demSoLanXuatHienChuoi(chuoi):
    # Khởi tạo từ điển để lưu trữ số lần xuất hiện của các từ
    tu_dien = {}

    # Chuyển đổi chuỗi thành chữ thường và tách thành các từ riêng biệt
    words = chuoi.lower().split()

    # Đếm số lần xuất hiện của từng từ
    for word in words:
        if word in tu_dien:
            tu_dien[word] += 1
        else:
            tu_dien[word] = 1

    return tu_dien

# Ví dụ sử dụng hàm
chuoi = "Lap trinh Python va AI — Truong Cong nghe va thiet ke – Dai Hoc UEH Thanh Pho Ho Chi Minh."
ket_qua = demSoLanXuatHienChuoi(chuoi)
print(ket_qua)


# Ví dụ sử dụng hàm
chuoi = "Lap trinh Python va AI — Truong Cong nghe va thiet ke – Dai Hoc UEH Thanh Pho Ho Chi Minh."
ket_qua = demSoLanXuatHienChuoi(chuoi)
print(ket_qua)