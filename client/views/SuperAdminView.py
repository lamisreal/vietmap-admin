from tkinter import *

from common.common import Common

class SuperAdminView:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (SuperAdminView._instance):
            return SuperAdminView._instance
        SuperAdminView._instance = SuperAdminView()
        return SuperAdminView._instance

    def __init__(self, root: Tk, super_admin, password):
        self.tkRoot = root
        self._common = Common()
        self._super_admin = super_admin
        self._password = password
        self._common.center_window(self.tkRoot, 610, 300)
        self.initView()

    def reuse(self):
        self.tkRoot = Tk()
        self._common.center_window(self.tkRoot, 610, 300)
        self.initView()

    def initView(self):
        root = self.tkRoot

        root.title("Chức năng admin")
        self.top_frame = Frame(root, padx=10, pady=10)
        self.top_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Header
        self.labelTitle = Label(self.top_frame, text="Xin chào tài khoản {0}".format(self._super_admin["username"]), font=("Arial", 20, "bold"))
        self.labelTitle.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Tạo button_frame
        self.button_frame = Frame(self.top_frame)
        self.button_frame.grid(row=1, column=0, columnspan=2, pady=20)

        # Hàng 1: "Thông tin cá nhân", "Đăng xuất"
        self.btnProfile = Button(self.button_frame, text="Thông tin cá nhân", font=("Arial", 10), width=20, relief="raised", bd=2)
        self.btnProfile.grid(row=0, column=0, padx=10, pady=5)

        self.btnDangXuat = Button(self.button_frame, text="Đăng xuất", font=("Arial", 10), width=20, relief="raised", bd=2)
        self.btnDangXuat.grid(row=0, column=1, padx=10, pady=5)
        
        # Hàng 2: "Danh sách tài khoản"
        self.btnDanhsachtk = Button(self.button_frame, text="Danh sách tài khoản", font=("Arial", 10), width=20, relief="raised", bd=2)
        self.btnDanhsachtk.grid(row=1, column=0, padx=10, pady=5)

    def showView(self):
        self.tkRoot.mainloop()