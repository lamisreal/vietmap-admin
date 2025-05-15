from tkinter import *
import uuid
from datetime import datetime

class Common:
    def center_window(self, root: Tk, width=800, height=600):
        # Lấy kích thước màn hình
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Lấy kích thước cửa sổ
        window_width = width
        window_height = height

        # Tính toán vị trí để căn giữa
        position_top = int(screen_height / 2 - window_height / 2)
        position_left = int(screen_width / 2 - window_width / 2)

        # Đặt vị trí cửa sổ
        root.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')
        
    def get_device_id(self):
        import platform
        import uuid
        import subprocess

        system = platform.system()

        if system == "Windows":
            try:
                result = subprocess.check_output('wmic csproduct get uuid', shell=True)
                return result.decode().split('\n')[1].strip()
            except:
                return str(uuid.getnode())
        
        elif system == "Linux":
            try:
                with open('/etc/machine-id', 'r') as f:
                    return f.read().strip()
            except:
                return str(uuid.getnode())
        
        elif system == "Darwin":  # macOS
            try:
                result = subprocess.check_output(['ioreg', '-rd1', '-c', 'IOPlatformExpertDevice'])
                for line in result.decode().split('\n'):
                    if "IOPlatformUUID" in line:
                        return line.split('=')[-1].strip().strip('"')
            except:
                return str(uuid.getnode())
        
        return str(uuid.getnode())
    
    def format_date(self, date_input):
        date_str = date_input
        date_obj = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S GMT")
        formatted_date = date_obj.strftime("%d/%m/%Y")
        return formatted_date
    
    def get_sex(self, sex_code_input):
        result = ""
        if sex_code_input == "M":
            result = "Nam"
        elif sex_code_input == "F":
            result = "Nữ"
        return result
    
    def get_sex_code(self, sex_input):
        result = ""
        if sex_input == "Nam":
            result = "M"
        elif sex_input == "Nữ":
            result = "F"
        return result