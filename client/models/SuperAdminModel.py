from common.common import Common
from models.connectDB import ConnectDB
import requests
import uuid

class SuperAdmin:
    def __init__(self):
        self.ID = None
        self.USERNAME = None
        self.EMAIL = None
        self.ROLE = None
        self.PASSWORD = None

class SuperAdminModel(ConnectDB):
    _instance = None

    @classmethod
    def getInstance(cls):
        if (SuperAdminModel._instance):
            return SuperAdminModel._instance
        SuperAdminModel._instance = SuperAdminModel()
        return SuperAdminModel._instance

    def __init__(self):
        self._common = Common()
        self._url = "http://127.0.0.1:5000/api/superadmin/"
        self._common = Common()
        self._device_id = self._common.get_device_id()
        self._device_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, self._device_id)
        
        super().__init__()
        
    def convertData(self, data):
        return 0

    def login(self, username: str, password: str):
        params = {
            "username": username,
            "password": password,
            "device_uuid": self._device_uuid  # bạn có thể truyền tham số này từ nơi khác nếu cần
        }
        url = self._url

        try:
            response = requests.get(url, params)
            if response.status_code == 200:
                data = response.json()
                superadmin = data["data"]

                # xử lý hoặc chuyển đổi dữ liệu nếu cần
                return superadmin
            else:
                print(f"Lỗi: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Lỗi kết nối API: {e}")
            return None