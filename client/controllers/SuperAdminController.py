from models.SuperAdminModel import SuperAdminModel
from views.SuperAdminView import SuperAdminView

from tkinter import *

from controllers.ThongTinCaNhanController import ThongTinCaNhanController
from models.ThongTinCaNhanModel import ThongTinCaNhanModel
from views.ThongTinCaNhanView import ThongTinCaNhanView


class SuperAdminController:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (SuperAdminController._instance):
            return SuperAdminController._instance
        SuperAdminController._instance = SuperAdminController()
        return SuperAdminController._instance

    def __init__(self, model: SuperAdminModel, view: SuperAdminView):
        self._model = model
        self._view = view
        
    def initItemView(self):
        self._view.btnProfile["command"] = self.goToProfileScreen
        if self.commandBack:
            def _back():
                self._view.tkRoot.destroy()
                self.commandBack()

            self._view.btnDangXuat["command"] = _back
        
        self.load_data()
        
    def load_data(self):
        """Hiển thị danh sách"""

    def goToProfileScreen(self):
        self._view.tkRoot.destroy()
        data = self._model.get_data_by_id(self._view._super_admin[0]["USERNAME"])
        root = Tk()
        m = ThongTinCaNhanModel()
        v = ThongTinCaNhanView(root, data)
        c = ThongTinCaNhanController(m, v)
        c.initCommandButtonBack(self.back)
    
    def back(self):
        self._view.reuse()
        self.initItemView()
        self._view.showView()

    def initCommandButtonDangXuat(self, commandBack):
         self.commandBack = commandBack