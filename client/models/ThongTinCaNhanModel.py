from models.connectDB import ConnectDB

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
        super().__init__()
    
    def convert_obj(self, row):
        data_convert = {
                        "USERNAME": row[1],
                        "HOTEN": row[2],
                        "GIOITINH": row[3],
                        "NGSINH": row[4]
                        }
        return data_convert
        
    def convert(self, data):
        return [self.convert_obj(row) for row in data]
    
    def load_item(self, item):
        """Trả về danh sách dữ liệu."""
        db = self.connect()
        cursor = db.cursor()
        query = "SELECT * FROM {0} WHERE USERNAME = %s".format(self.NAME_TABLE_INFORMATION)
        cursor.execute(query, (item[0]["USERNAME"]))
        data = cursor.fetchone()
        self.close()
        
        return self.convert_obj(data)
    
    def check_same(self, item, item_old): 
    # Chuyển đổi các giá trị về cùng một kiểu (sang chuỗi) trước khi so sánh
        if (str(item["USERNAME"]) != str(item_old["USERNAME"]) or
            str(item["HOTEN"]) != str(item_old["HOTEN"]) or
            str(item["GIOITINH"]) != str(item_old["GIOITINH"]) or
            str(item["NGSINH"]) != str(item_old["NGSINH"])):
            return False
        return True
    
    def update_item(self, item):
        """Thêm dữ liệu mới vào CSDL."""
        db = self.connect()
        cursor = db.cursor()
        try:
            query = """
                    UPDATE {0}
                    SET HOTEN = %s, GIOITINH = %s, NGSINH = %s
                    WHERE USERNAME = %s
                    """.format(self.NAME_TABLE_INFORMATION)

            cursor.execute(query, (item["HOTEN"], item["GIOITINH"], item["NGSINH"], item["USERNAME"]))
            db.commit()
            
            return "UPDATED"
        except Exception as e:
            db.rollback()
            print(f"Lỗi khi cập nhật dữ liệu: {e}")
            return "ERROR"
        finally:
            self.close()