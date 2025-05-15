from tkinter import *
from tkinter import messagebox

from controllers.SuperAdminController import SuperAdminController
from models.SuperAdminModel import SuperAdminModel
from views.SuperAdminView import SuperAdminView

from common.common import Common


class LoginView:
    _instance = None
    
    @classmethod
    def getInstance(cls):
        if (LoginView._instance):
            return LoginView._instance
        LoginView._instance = LoginView()
        return LoginView._instance

    def __init__(self):
        self.tkRoot = Tk()
        self._common = Common()
        self._common.center_window(self.tkRoot, 500, 300)
    
    def initView(self):
        root = self.tkRoot
        username = "superadmin1"
        password = "123456"

        root.title("Đăng nhập")
        self.top_frame = Frame(root, padx=10, pady=10)
        self.top_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        #Creating layout of login form
        Label(root, text="Hãy điền các thông tin cần thiết", width="300", bg="orange",fg="white").pack()
        
        # Tiêu đề
        self.labelTitle = Label(self.top_frame, text="Đăng Nhập", font=("Arial", 20, "bold"))
        self.labelTitle.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Tên đăng nhập
        self.label_inputUserName = Label(self.top_frame, text="Tên đăng nhập *: ", font=("Arial", 10, "bold"))
        self.label_inputUserName.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_inputUserName_text = StringVar(value=username)
        self.inputUserName = Entry(self.top_frame, textvariable=self.entry_inputUserName_text, width=40, font=("Arial", 10))
        self.inputUserName.grid(row=1, column=1, padx=10, pady=5)

        # Mật khẩu
        self.label_inputPassword = Label(self.top_frame, text="Mật khẩu *: ", font=("Arial", 10, "bold"))
        self.label_inputPassword.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_inputPassword_text = StringVar(value=password)
        self.inputPassword = Entry(self.top_frame, textvariable=self.entry_inputPassword_text, width=40, font=("Arial", 10), show='*')
        self.inputPassword.grid(row=2, column=1, padx=10, pady=5)
        
        #login
        self.button_frame = Frame(self.top_frame)
        self.button_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

        self.buttonRefresh = Button(self.button_frame, text="Đăng nhập", font=("Arial", 10), width=20, relief="raised", bd=2, command=self.loginManHinh)
        self.buttonRefresh.grid(row=0, column=0, padx=10)

    def showView(self):
        self.tkRoot.mainloop()

    def loginManHinh(self):
        """Lấy thông tin userName và password, và xử lý."""
        userName = self.inputUserName.get()
        password = self.inputPassword.get()
        
        # Kiểm tra thông tin đầu vào (có thể mở rộng kiểm tra)
        if not userName or not password:
            messagebox.showerror("Cảnh báo", "Hãy điền đầy đủ Tên đăng nhập và Mật khẩu!")
        else:
            superadmin = SuperAdminModel.getInstance().login(userName, password)
            if (superadmin):
                # messagebox.showinfo("Thành công", f"Đăng nhập thành công, xin chào \"{superadmin["username"]}\"")
                self.tkRoot.destroy()
                root = Tk()
                m = SuperAdminModel()
                v = SuperAdminView(root, superadmin, password)
                c = SuperAdminController(m, v)
                c.initCommandButtonDangXuat(self.back)
                c.initItemView()
                v.showView()
            else:
                messagebox.showerror("Thất bại", "Tài khoản hoặc mật khẩu admin không chính xác")

    def reuse(self):
        self.tkRoot = Tk()
        self._common.center_window(self.tkRoot, 500, 300)
        self.initView()

    def back(self):
        self.reuse()
        self.showView()