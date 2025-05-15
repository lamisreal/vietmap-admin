from models.connectDB import ConnectDB
import requests
from datetime import datetime
from common.common import Common

class DanhSachTaiKhoan:
    def __init__(self, username, hoten, email, role, gioitinh, ngsinh):
        self._username = username
        self._hoten = hoten
        self._email = email
        self._role = role
        self._gioitinh = gioitinh
        self._ngsinh = ngsinh


class DanhSachTaiKhoanModel(ConnectDB):
    _instance = None
    
    @classmethod
    def getInstance(cls):
        if (DanhSachTaiKhoanModel._instance):
            return DanhSachTaiKhoanModel._instance
        DanhSachTaiKhoanModel._instance = DanhSachTaiKhoanModel()
        return DanhSachTaiKhoanModel._instance
    
    def __init__(self, username: str):
        self._url_superadmin = "http://127.0.0.1:5000/api/superadmin"
        self._common = Common()
        self._device_id = self._common.get_device_id()
        self._username = username
        super().__init__()
    
    def convert_obj(self, row):
        data_convert = {
            "username": row["username"],
            "hoten": row["hoten"],
            "email": row["email"],
            "role": row["role"],
            "gioitinh": self._common.get_sex(row["gioitinh"]),
            "ngsinh": self._common.format_date(row["ngsinh"])
            }
        
        return data_convert
    
    def convert(self, data):
        return [self.convert_obj(row) for row in data]
    
    def get_list_data(self, username, password):
        """Trả về danh sách dữ liệu."""
        params = {
            "username": username,
            "password": password
        }
        url = self._url_superadmin + "/get_all"

        try:
            response = requests.get(url, params)
            if response.status_code == 200:
                data = response.json()
                all_data = self.convert(data["data"])
                return all_data
            else:
                print(f"Lỗi: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Lỗi kết nối API: {e}")
            return None
        
    def add_item(self, item):
        """Thêm dữ liệu mới vào CSDL."""
        payload = {
                   "username_superadmin": self._username,
                   "username": item["username"],
                   "hoten": item["hoten"],
                   "email": item["email"],
                   "role": item["role"],
                   "gioitinh": item["gioitinh"],
                   "ngsinh": item["ngsinh"]
                   }
        
        url = self._url_superadmin + "/create_account_user"

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print(f"Lỗi: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Lỗi kết nối API: {e}")
            return None

    def update_item(self, item):
        """Thêm dữ liệu mới vào CSDL."""
        return

    def delete_item(self, item):
        """Xoá dữ liệu CSDL."""
        return