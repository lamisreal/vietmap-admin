from models.connectDB import ConnectDB
import requests

class ThongTinCaNhan:
    def __init__(self, USERNAME, HOTEN, GIOITINH, NGSINH):
        self._USERNAME = USERNAME
        self._HOTEN = HOTEN
        self._GIOITINH = GIOITINH
        self._NGSINH = NGSINH


class ThongTinCaNhanModel(ConnectDB):
    _instance = None
    
    @classmethod
    def getInstance(cls):
        if (ThongTinCaNhanModel._instance):
            return ThongTinCaNhanModel._instance
        ThongTinCaNhanModel._instance = ThongTinCaNhanModel()
        return ThongTinCaNhanModel._instance
    
    def __init__(self):
        self._url_superadmin = "http://127.0.0.1:5000/api/superadmin/"
        self._url_information = "http://127.0.0.1:5000/api/information/"
        super().__init__()
    
    def get_information_by_username(self, username: str):
        params = {
            "username": username
        }
        url = self._url_superadmin + "/get_admin_by_username"

        try:
            response = requests.get(url, params)
            if response.status_code == 200:
                data = response.json()
                superadmin_info = data["data"]
                return superadmin_info
            else:
                print(f"Lỗi: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Lỗi kết nối API: {e}")
            return None
    
    def update_item(self, item):
        payload = item
        url = self._url_information + "/update"

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # xử lý hoặc chuyển đổi dữ liệu nếu cần
                return data
            else:
                print(f"Lỗi: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Lỗi kết nối API: {e}")
            return None
        