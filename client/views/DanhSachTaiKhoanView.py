from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry
from datetime import datetime

from common.common import Common

class DanhSachTaiKhoanView:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (DanhSachTaiKhoanView._instance):
            return DanhSachTaiKhoanView._instance
        DanhSachTaiKhoanView._instance = DanhSachTaiKhoanView()
        
        return DanhSachTaiKhoanView._instance

    def __init__(self, root: Tk, username: str, password: str):
        self._root = root
        self._tree = ttk.Treeview(None)
        self._common = Common()
        self._common.center_window(root)
        self.initView()
        self._username = username
        self._password = password
        
    @property
    def tree(self):
        return self._tree
    
    @property
    def username_param(self):
        return self._username
    
    @property
    def password_param(self):
        return self._password
    
    def initView(self):
        root = self._root

        root.title("Danh sách tài khoản")
        self.top_frame = Frame(root, padx=10, pady=10)
        self.top_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.top_frame.grid_rowconfigure(0, weight=1)  # Chỉ định row 0 có thể thay đổi kích thước
        self.top_frame.grid_columnconfigure(0, weight=1)  # Chỉ định cột 0 có thể thay đổi kích thước
        self.top_frame.grid_columnconfigure(1, weight=2)
        self.top_frame.grid_columnconfigure(2, weight=2)
        self.top_frame.grid_columnconfigure(3, weight=3)
        
        self.header()
        self.body()

    def header(self):
        """Tạo các ô nhập liệu."""
        # Tiêu đề
        self.labelTitle = Label(self.top_frame, text="Danh sách tài khoản", font=("Arial", 20, "bold"))
        self.labelTitle.grid(row=0, column=0, columnspan=2, pady=10)

        # Tên đăng nhập
        self.label_user_name = Label(self.top_frame, text="Tên đăng nhập: ", font=("Arial", 10, "bold"))
        self.label_user_name.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_user_name_text = StringVar()
        self.user_name = Entry(self.top_frame, textvariable=self.entry_user_name_text, width=40, font=("Arial", 10))
        self.user_name.grid(row=1, column=1, padx=10, pady=5)

        # Họ tên
        self.label_ho_ten = Label(self.top_frame, text="Họ tên: ", font=("Arial", 10, "bold"))
        self.label_ho_ten.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_ho_ten_text = StringVar()
        self.ho_ten = Entry(self.top_frame, textvariable=self.entry_ho_ten_text, width=40, font=("Arial", 10))
        self.ho_ten.grid(row=2, column=1, padx=10, pady=5)

        # Email
        self.label_email = Label(self.top_frame, text="Email: ", font=("Arial", 10, "bold"))
        self.label_email.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_email_text = StringVar()
        self.email = Entry(self.top_frame, textvariable=self.entry_email_text, width=40, font=("Arial", 10))
        self.email.grid(row=3, column=1, padx=10, pady=5)
        
        # Role
        self.label_role = Label(self.top_frame, text="Role: ", font=("Arial", 10, "bold"))
        self.label_role.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.role_var = StringVar()
        self.role = ttk.Combobox(self.top_frame, textvariable=self.role_var, width=37, font=("Arial", 10))
        self.role['values'] = ("superadmin", "admin")  # Dropdown options
        self.role.grid(row=4, column=1, padx=10, pady=5)
        
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
        self.button_frame.grid(row=8, column=0, columnspan=2, pady=20)

        self.buttonRefresh = Button(self.button_frame, text="Làm mới", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonRefresh.grid(row=0, column=0, padx=10)

        self.buttonAdd = Button(self.button_frame, text="Thêm", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonAdd.grid(row=0, column=1, padx=10)

        self.buttonEdit = Button(self.button_frame, text="Cập nhật", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonEdit.grid(row=0, column=2, padx=10)

        self.buttonRemove = Button(self.button_frame, text="Xoá", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonRemove.grid(row=0, column=3, padx=10)

        self.buttonBack = Button(self.button_frame, text="Trở về", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonBack.grid(row=0, column=4, padx=10)

    def body(self):
        """Tạo bảng Treeview."""
        self._tree = ttk.Treeview(
            self._root, columns=("username", "hoten", "email", "role", "gioitinh", "ngsinh"), show="headings"
        )
        self._tree.pack(fill="both", expand=True, padx=10, pady=10)

        self._tree.heading("username", text="Tên đăng nhập")
        self._tree.heading("hoten", text="Họ & tên")
        self._tree.heading("email", text="Email")
        self._tree.heading("role", text="Role")
        self._tree.heading("gioitinh", text="Giới tính")
        self._tree.heading("ngsinh", text="Ngày sinh")

        self._tree.column("username", width=20, anchor="center")
        self._tree.column("hoten", width=30, anchor="w")
        self._tree.column("email", width=50, anchor="w")
        self._tree.column("role", width=15, anchor="center")
        self._tree.column("gioitinh", width=10, anchor="center")
        self._tree.column("ngsinh", width=20, anchor="center")

    #get
    def get_selected_item(self):
        """Trả về của item được chọn."""
        selected_items = self._tree.selection()
        
        if selected_items:  
            first_item = selected_items[0]  
            values = self._tree.item(first_item, "values")  
            return values
        else:
            return None

    def get_input_values(self):
        """Lấy dữ liệu từ các ô nhập liệu."""
        return {
            "username": self.get_user_name(),
            "hoten": self.get_ho_ten(),
            "email": self.get_email(),
            "role": self.get_role(),
            "gioitinh": self.get_gioi_tinh(),
            "ngsinh": self.get_ngay_sinh()
        }
        
    def get_user_name(self):
        return self.entry_user_name_text.get()
        
    def get_ho_ten(self):
        return self.entry_ho_ten_text.get()
        
    def get_email(self):
        return self.entry_email_text.get()
        
    def get_role(self):
        return self.role_var.get()
        
    def get_gioi_tinh(self):
        value = self.gioi_tinh_var.get()
        if value == "Nam":
            result = 'M'
        elif value == "Nữ":
            result = 'F'
        return result
    
    def get_ngay_sinh(self):
        return self.ngay_sinh.get_date().strftime("%Y-%m-%d")

    #set
    def set_user_name(self, user_name):
        self.entry_user_name_text.set(user_name)

    def set_ho_ten(self, ho_ten):
        self.entry_ho_ten_text.set(ho_ten)

    def set_email(self, email):
        self.entry_email_text.set(email)

    def set_role(self, value):
        self.role_var.set(value)
            
    def set_gioi_tinh(self, value):
        if value == 'M':
            self.gioi_tinh_var.set("Nam")
        elif value == 'F':
            self.gioi_tinh_var.set("Nữ")

    def set_ngay_sinh(self, ngay_sinh):
        self.ngay_sinh.set_date(datetime.strptime(ngay_sinh, "%d/%m/%Y").date())

    def clear_inputs(self):
        """Xóa nội dung các ô nhập liệu."""
        self.user_name.delete(0, END)
        self.ho_ten.delete(0, END)
        self.email.delete(0, END)
        self.role.delete(0, END)
        self.gioi_tinh.delete(0, END)
        self.ngay_sinh.set_date(datetime.now().date())
        
    def load_list(self, data):
        """Cập nhật Treeview với dữ liệu."""
        for item in self._tree.get_children():
            self._tree.delete(item)

        for item in data:
            self._tree.insert("", END, values=(item["username"], item["hoten"], item["email"], item["role"], item["gioitinh"], item["ngsinh"]))
        
    def showView(self):
        self._root.mainloop()