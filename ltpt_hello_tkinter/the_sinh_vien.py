import tkinter as tk
root = tk.Tk()
root.title("Thẻ Sinh Viên Số")
# Kích thước cửa sổ
root.geometry("400x300")
# Đổi màu nền toàn bộ cửa sổ
root.configure(bg="#f8f9fa")

# TIÊU ĐỀ 
nhan_truong = tk.Label(
    root,
    text="TRƯỜNG ĐẠI HỌC HẠ LONG",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#0056b3"
)

nhan_truong.pack(fill="x", pady=10)

# HỌ TÊN 
nhan_ten = tk.Label(
    root,
    text="Họ tên: Nguyễn Văn A",
    font=("Arial", 12),
    bg="#f8f9fa"
)

nhan_ten.pack(pady=5)

# MSSV 
nhan_msv = tk.Label(
    root,
    text="MSSV: 22010001",
    font=("Arial", 12),
    fg="red",
    bg="#f8f9fa"
)

nhan_msv.pack(pady=5)


# KHOA 
nhan_khoa = tk.Label(
    root,
    text="Khoa: Công nghệ thông tin",
    font=("Arial", 12),
    fg="green",
    bg="#f8f9fa"
)

nhan_khoa.pack(pady=5)


# NÚT THOÁT
nut_thoat = tk.Button(
    root,
    text="Đóng ứng dụng",
    command=root.destroy,
    bg="#dc3545",
    fg="white",
    width=20,
    height=2,
    font=("Arial", 11, "bold")
)

nut_thoat.pack(pady=20)

# Chạy ứng dụng
root.mainloop()