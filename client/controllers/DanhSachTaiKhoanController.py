from tkinter import messagebox
from models.DanhSachTaiKhoanModel import DanhSachTaiKhoanModel
from views.DanhSachTaiKhoanView import DanhSachTaiKhoanView
from common.common import Common

class DanhSachTaiKhoanController:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (DanhSachTaiKhoanController._instance):
            return DanhSachTaiKhoanController._instance
        DanhSachTaiKhoanController._instance = DanhSachTaiKhoanController()
        return DanhSachTaiKhoanController._instance

    def __init__(self, model: DanhSachTaiKhoanModel, view: DanhSachTaiKhoanView):
        self._model = model
        self._view = view
        self._tree = self._view.tree
        self._common = Common()
        self._view.user_name.bind('<KeyRelease>', self.user_name_text_change)
        self._view.ho_ten.bind('<KeyRelease>', self.field_text_change)
        self._view.email.bind('<KeyRelease>', self.field_text_change)
        self._view.role.bind('<<ComboboxSelected>>', self.field_text_change)
        self._view.gioi_tinh.bind('<<ComboboxSelected>>', self.field_text_change)
        self._view.ngay_sinh.bind("<<DateEntrySelected>>", self.field_text_change)
        self._view.buttonRefresh["command"] = self.btn_refresh
        self._view.buttonAdd["command"] = self.add_item
        self._view.buttonEdit["command"] = self.update_item
        self._view.buttonRemove["command"] = self.delete_item
        self._view.tree.bind('<<TreeviewSelect>>', self.get_selected_item)
        
        self.load_data()
            
    def load_data(self):
        """Hiển thị danh sách"""
        data = self._model.get_list_data(self._view.username_param, self._view.password_param)
        self._view.load_list(data)
        self._view.buttonEdit.config(state="disabled")
        self._view.buttonRemove.config(state="disabled")

    def user_name_text_change(self, event=None):
        self._view.buttonRefresh.config(state="normal")
        self._view.buttonAdd.config(state="normal")
        
    def ma_key_text_change(self, event=None):
        self._view.buttonRefresh.config(state="normal")
        self._view.buttonAdd.config(state="normal")
        self._view.buttonEdit.config(state="disabled")
        self._view.buttonRemove.config(state="disabled")

    def field_text_change(self, event=None):
        self._view.buttonRefresh.config(state="normal")
        self._view.buttonAdd.config(state="normal")
        self._view.buttonEdit.config(state="normal")
        self._view.buttonRemove.config(state="normal")

    def btn_refresh(self):
        self._view.buttonEdit.config(state="disabled")
        self._view.buttonRemove.config(state="disabled")
        self._view.user_name.config(state='normal')
        self._view.clear_inputs()
        self.load_data()
        
    def add_item(self):
        """Thêm dữ liệu"""
        item = self._view.get_input_values()
        if any(value == "" for value in item.values()):
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin.")
            return
        
        data = self._model.add_item(item)
        messagebox.showinfo("Thông báo", data["message"])
        self._view.clear_inputs()
        self.load_data()

    def update_item(self):
        """Chỉnh sửa dữ liệu"""
        ma = self._view.get_selected_item()
        if ma is None:
            messagebox.showerror("Lỗi", "Vui lòng chọn một dòng để sửa.")
            return

        item = self._view.get_input_values()
        status = self._model.update_item(item)
        if status == "UPDATED":
            messagebox.showinfo("Thông báo", "Cập nhật thành công")
            self._view.clear_inputs()
        elif status == "NONE":
            messagebox.showinfo("Thông báo", "Dữ liệu không bị thay đổi, không cần cập nhật")
        else:
            messagebox.showerror("Thông báo", "Lôi thao tác")
        self.load_data()
        
    def delete_item(self):
        """Xoá dữ liệu đã chọn"""
        ma = self._view.get_selected_item()
        
        if ma is None:
            messagebox.showerror("Lỗi", "Vui lòng chọn một dòng để xóa.")
            return

        # Hiển thị hộp thoại xác nhận
        confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa không?")
        
        if confirm:  # Nếu người dùng nhấn "Yes"
            item = self._view.get_input_values()
            self._model.delete_item(item)
            self.load_data()
            messagebox.showinfo("Thông báo", "Xóa thành công.")
        
    def get_selected_item(self, event=None):
        """Hàm xử lý khi người dùng chọn một mục trong Treeview."""
        self._view.buttonAdd.config(state="normal")
        self._view.buttonRemove.config(state="normal")
        
        self._view.clear_inputs()
        tk = self._view.get_selected_item()
        if tk != None:
            username = tk[0]
            hoten = tk[1]
            email = tk[2]
            role = tk[3]
            gioitinh = self._common.get_sex_code(tk[4])
            ngsinh = tk[5]
            
            self._view.set_user_name(username)
            self._view.set_ho_ten(hoten)
            self._view.set_email(email)
            self._view.set_role(role)
            self._view.set_gioi_tinh(gioitinh)
            self._view.set_ngay_sinh(ngsinh)
            self._view.user_name.config(state='disabled')

    def initCommandButtonBack(self, commandBack):
        if commandBack:
            def back():
                self._view._root.destroy()
                commandBack()

            self._view.buttonBack["command"] = back