from tkinter import messagebox
from models.ThongTinCaNhanModel import ThongTinCaNhanModel
from views.ThongTinCaNhanView import ThongTinCaNhanView

class ThongTinCaNhanController:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (ThongTinCaNhanController._instance):
            return ThongTinCaNhanController._instance
        ThongTinCaNhanController._instance = ThongTinCaNhanController()
        return ThongTinCaNhanController._instance

    def __init__(self, model: ThongTinCaNhanModel, view: ThongTinCaNhanView):
        self._model = model
        self._view = view
        self._view.user_name.bind('<KeyRelease>', self.user_name_text_change)
        self._view.ho_ten.bind('<KeyRelease>', self.field_text_change)
        self._view.gioi_tinh.bind('<<ComboboxSelected>>', self.field_text_change)
        self._view.ngay_sinh.bind("<<DateEntrySelected>>", self.field_text_change)
        self._view.buttonRefresh["command"] = self.btn_refresh
        self._view.buttonEdit["command"] = self.update_item
        
        self.load_data()
            
    def load_data(self):
        """Hiển thị danh sách"""
        data = self._model.load_item(self._view.super_admin_param)
        self._view.set_input_values(data)
        self._view.buttonRefresh.config(state="normal")
        self._view.buttonEdit.config(state="disabled")

    def user_name_text_change(self, event=None):
        self._view.buttonRefresh.config(state="normal")
        self._view.buttonEdit.config(state="disabled")

    def field_text_change(self, event=None):
        self._view.buttonRefresh.config(state="normal")
        self._view.buttonEdit.config(state="normal")

    def btn_refresh(self):
        self._view.buttonEdit.config(state="disabled")
        self.load_data()

    def update_item(self):
        """Chỉnh sửa dữ liệu"""
        item = self._view.get_input_values()
        status = self._model.update_item(item)
        if status == "UPDATED":
            messagebox.showinfo("Thông báo", "Cập nhật thành công")
            self._view.clear_inputs()
        elif status == "NONE":
            messagebox.showinfo("Thông báo", "Dữ liệu không bị thay đổi, không cần cập nhật")
        else:
            messagebox.showerror("Thông báo", "Lỗi thao tác")
        self.load_data()

    def initCommandButtonBack(self, commandBack):
        if commandBack:
            def back():
                self._view._root.destroy()
                commandBack()

            self._view.buttonBack["command"] = back