from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry
from datetime import datetime

from common.common import Common

class ThongTinCaNhanView:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (ThongTinCaNhanView._instance):
            return ThongTinCaNhanView._instance
        ThongTinCaNhanView._instance = ThongTinCaNhanView()
        
        return ThongTinCaNhanView._instance

    def __init__(self, root: Tk, super_admin):
        self._root = root
        self._super_admin = super_admin
        self._common = Common()
        self._common.center_window(root, 500, 500)
        self.initView()
    
    
    @property
    def super_admin_param(self):
        return self._super_admin
    
    def initView(self):
        root = self._root

        root.title("Thông tin admin")
        self.top_frame = Frame(root, padx=10, pady=10)
        self.top_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.top_frame.grid_rowconfigure(0, weight=1)  # Chỉ định row 0 có thể thay đổi kích thước
        self.top_frame.grid_columnconfigure(0, weight=1)  # Chỉ định cột 0 có thể thay đổi kích thước
        self.top_frame.grid_columnconfigure(1, weight=2)
        self.top_frame.grid_columnconfigure(2, weight=2)
        self.top_frame.grid_columnconfigure(3, weight=3)
        self.top_frame.grid_columnconfigure(4, weight=4)
        
        self.header()

    def header(self):
        """Tạo các ô nhập liệu."""
        # Tiêu đề
        self.labelTitle = Label(self.top_frame, text="Thông tin người dùng", font=("Arial", 20, "bold"))
        self.labelTitle.grid(row=0, column=0, columnspan=2, pady=10)

        # Tên đăng nhập
        self.label_user_name = Label(self.top_frame, text="Tên đăng nhập: ", font=("Arial", 10, "bold"))
        self.label_user_name.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_user_name_text = StringVar()
        self.user_name = Entry(self.top_frame, textvariable=self.entry_user_name_text, width=40, font=("Arial", 10), state="disabled")
        self.user_name.grid(row=1, column=1, padx=10, pady=5)

        # Họ tên
        self.label_ho_ten = Label(self.top_frame, text="Họ tên: ", font=("Arial", 10, "bold"))
        self.label_ho_ten.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_ho_ten_text = StringVar()
        self.ho_ten = Entry(self.top_frame, textvariable=self.entry_ho_ten_text, width=40, font=("Arial", 10))
        self.ho_ten.grid(row=2, column=1, padx=10, pady=5)
        
        # Giới tính
        self.label_gioi_tinh = Label(self.top_frame, text="Giới tính: ", font=("Arial", 10, "bold"))
        self.label_gioi_tinh.grid(row=5, column=0, padx=10, pady=5, sticky="e")

        self.gioi_tinh_var = StringVar()
        self.gioi_tinh = ttk.Combobox(self.top_frame, textvariable=self.gioi_tinh_var, width=37, font=("Arial", 10))
        self.gioi_tinh['values'] = ("Nam", "Nữ")  # Dropdown options
        self.gioi_tinh.grid(row=5, column=1, padx=10, pady=5)

        # Ngày sinh
        self.label_ngay_sinh = Label(self.top_frame, text="Ngày sinh: ", font=("Arial", 10, "bold"))
        self.label_ngay_sinh.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.ngay_sinh = DateEntry(self.top_frame, width=41, background="darkblue", foreground="white", borderwidth=2, date_pattern="dd/mm/yyyy")
        self.ngay_sinh.grid(row=6, column=1, padx=10, pady=5)

        # Các nút chức năng
        self.button_frame = Frame(self.top_frame)
        self.button_frame.grid(row=11, column=0, columnspan=2, pady=20)

        self.buttonRefresh = Button(self.button_frame, text="Làm mới", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonRefresh.grid(row=0, column=0, padx=10)

        self.buttonEdit = Button(self.button_frame, text="Cập nhật", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonEdit.grid(row=0, column=1, padx=10)

        self.buttonBack = Button(self.button_frame, text="Trở về", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonBack.grid(row=0, column=2, padx=10)

    def get_input_values(self):
        """Lấy dữ liệu từ các ô nhập liệu."""
        return {
            "USERNAME": self.get_user_name(),
            "HOTEN": self.get_ho_ten(),
            "GIOITINH": self.get_gioi_tinh(),
            "NGSINH": self.get_ngay_sinh(),
        }

    def set_input_values(self, item):
        """Lấy dữ liệu từ DB vào các ô nhập liệu."""
        self.set_user_name(str(item["USERNAME"]))
        self.set_ho_ten(str(item["HOTEN"]))
        self.set_gioi_tinh(str(item["GIOITINH"]))
        self.set_ngay_sinh(str(item["NGSINH"]))
        
    def get_user_name(self):
        return self.entry_user_name_text.get()
    
    def get_ho_ten(self):
        return self.entry_ho_ten_text.get()
    
    def get_gioi_tinh(self):
        value = self.gioi_tinh_var.get()
        if value == "Nam":
            result = 'M'
        elif value == "Nữ":
            result = 'F'
        return result
    
    def get_ngay_sinh(self):
        return self.ngay_sinh.get_date()

    #set
    def set_user_name(self, value):
        self.entry_user_name_text.set(value)

    def set_ho_ten(self, value):
        self.entry_ho_ten_text.set(value)

    def set_gioi_tinh(self, value):
        if value == 'M':
            self.gioi_tinh_var.set("Nam")
        elif value == 'F':
            self.gioi_tinh_var.set("Nữ")

    def set_ngay_sinh(self, ngay_sinh):
        self.ngay_sinh.set_date(datetime.strptime(ngay_sinh, "%Y-%m-%d %H:%M:%S").date())

    def clear_inputs(self):
        """Xóa nội dung các ô nhập liệu."""
        self.user_name.delete(0, END)
        self.ho_ten.delete(0, END)
        self.gioi_tinh.delete(0, END)
        self.ngay_sinh.set_date(datetime.now().date())
        
    def showView(self):
        self._root.mainloop()