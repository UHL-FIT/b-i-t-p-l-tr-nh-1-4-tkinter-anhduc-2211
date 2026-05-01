import tkinter as tk
# TẠO CỬA SỔ CHÍNH
root = tk.Tk()
root.title("Quản lý Sinh viên - UHL")
root.geometry("500x300")

# Màu nền cửa sổ
root.configure(bg="#f8f9fa")

# CHO CỘT 1 ĐƯỢC CO GIÃN
root.columnconfigure(1, weight=1)

# TIÊU ĐỀ
tieu_de = tk.Label(
    root,
    text="FORM NHẬP THÔNG TIN SINH VIÊN",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="#0056b3",
    pady=10
)

tieu_de.grid(
    row=0,
    column=0,
    columnspan=2,
    sticky="ew",
    pady=(0, 20)
)

# MÃ SINH VIÊN
nhan_ma_sv = tk.Label(
    root,
    text="Mã sinh viên:",
    font=("Arial", 11),
    bg="#f8f9fa"
)

nhan_ma_sv.grid(
    row=1,
    column=0,
    padx=15,
    pady=10,
    sticky="w"
)

o_nhap_ma_sv = tk.Entry(
    root,
    font=("Arial", 11)
)

o_nhap_ma_sv.grid(
    row=1,
    column=1,
    padx=15,
    pady=10,
    sticky="ew"
)

# HỌ TÊN
nhan_ho_ten = tk.Label(
    root,
    text="Họ và tên:",
    font=("Arial", 11),
    bg="#f8f9fa"
)

nhan_ho_ten.grid(
    row=2,
    column=0,
    padx=15,
    pady=10,
    sticky="w"
)

o_nhap_ho_ten = tk.Entry(
    root,
    font=("Arial", 11)
)

o_nhap_ho_ten.grid(
    row=2,
    column=1,
    padx=15,
    pady=10,
    sticky="ew"
)

# LỚP HỌC
nhan_lop = tk.Label(
    root,
    text="Lớp:",
    font=("Arial", 11),
    bg="#f8f9fa"
)

nhan_lop.grid(
    row=3,
    column=0,
    padx=15,
    pady=10,
    sticky="w"
)

o_nhap_lop = tk.Entry(
    root,
    font=("Arial", 11)
)

o_nhap_lop.grid(
    row=3,
    column=1,
    padx=15,
    pady=10,
    sticky="ew"
)

# NÚT BẤM
khung_nut = tk.Frame(root, bg="#f8f9fa")

khung_nut.grid(
    row=4,
    column=0,
    columnspan=2,
    pady=25
)

nut_luu = tk.Button(
    khung_nut,
    text="Lưu thông tin",
    bg="#198754",
    fg="white",
    font=("Arial", 11, "bold"),
    width=15,
    height=2
)

nut_luu.pack(side="left", padx=10)

nut_thoat = tk.Button(
    khung_nut,
    text="Thoát",
    command=root.destroy,
    bg="#dc3545",
    fg="white",
    font=("Arial", 11, "bold"),
    width=10,
    height=2
)

nut_thoat.pack(side="left", padx=10)

# CHẠY CHƯƠNG TRÌNH
root.mainloop()