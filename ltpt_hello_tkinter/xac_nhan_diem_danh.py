import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# HÀM XỬ LÝ DỮ LIỆU
def xu_ly_du_lieu():

    # Lấy dữ liệu từ ô nhập
    mssv = o_nhap_ma_sv.get()
    ho_ten = o_nhap_ho_ten.get()

    # Lấy thời gian hiện tại
    thoi_gian = datetime.now().strftime("%H:%M:%S")

    if mssv == "" or ho_ten == "":
        messagebox.showerror(
            "Lỗi",
            "Vui lòng nhập đầy đủ thông tin!"
        )
        return

    # Nếu MSSV không phải số
    if not mssv.isdigit():
        messagebox.showerror(
            "Lỗi dữ liệu",
            "Mã sinh viên phải là số!"
        )
        return

    # IN RA TERMINAL
    print("===== THÔNG TIN ĐIỂM DANH =====")
    print(f"Thời gian: {thoi_gian}")
    print(f"MSSV: {mssv}")
    print(f"Họ tên: {ho_ten}")
    print("===============================")

    # HIỂN THỊ LÊN GIAO DIỆN
    nhan_ket_qua.config(
        text=f"Đã xác nhận: {ho_ten} ({mssv})",
        fg="blue"
    )

    # XÓA Ô NHẬP SAU KHI XONG
    o_nhap_ma_sv.delete(0, tk.END)
    o_nhap_ho_ten.delete(0, tk.END)


# TẠO CỬA SỔ
root = tk.Tk()

root.title("Quản lý Sinh viên - UHL")
root.geometry("500x350")
root.configure(bg="#f8f9fa")

# Cho cột nhập liệu co giãn
root.columnconfigure(1, weight=1)

# TIÊU ĐỀ
tieu_de = tk.Label(
    root,
    text="XÁC NHẬN ĐIỂM DANH SINH VIÊN",
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
tk.Label(
    root,
    text="Mã sinh viên:",
    font=("Arial", 11),
    bg="#f8f9fa"
).grid(
    row=1,
    column=0,
    padx=10,
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
    padx=10,
    pady=10,
    sticky="ew"
)

# HỌ TÊN
tk.Label(
    root,
    text="Họ và tên:",
    font=("Arial", 11),
    bg="#f8f9fa"
).grid(
    row=2,
    column=0,
    padx=10,
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
    padx=10,
    pady=10,
    sticky="ew"
)

# NÚT XÁC NHẬN
nut_xac_nhan = tk.Button(
    root,
    text="Xác nhận điểm danh",
    command=xu_ly_du_lieu,
    bg="#198754",
    fg="white",
    font=("Arial", 11, "bold"),
    width=20,
    height=2
)

nut_xac_nhan.grid(
    row=3,
    column=0,
    columnspan=2,
    pady=20
)

# NHÃN KẾT QUẢ
nhan_ket_qua = tk.Label(
    root,
    text="Chưa có dữ liệu",
    font=("Arial", 11, "italic"),
    fg="gray",
    bg="#f8f9fa"
)

nhan_ket_qua.grid(
    row=4,
    column=0,
    columnspan=2,
    pady=20
)

# CHẠY CHƯƠNG TRÌNH
root.mainloop()