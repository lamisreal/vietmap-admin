import pymysql

class ConnectDB:
    # Field Connect
    _host="sql12.freesqldatabase.com"
    _user="sql12778065"
    _password="MwNsbUXzrb"
    _database="sql12778065"
    _port=3306
    
    # Field Table name
    NAME_TABLE_SUPERADMIN = "superadmin"
    NAME_TABLE_INFORMATION = "information"
    
    #Role
    ROLE_SUPERADMIN = "superadmin"
    ROLE_ADMIN = "admin"

    def __init__(self):
        self.connection = None
    
    # Kết nối đến cơ sở dữ liệu
    def connect(self):
        if self.connection is None or not self.connection.open:
            return pymysql.connect(
                host=self._host,
                user=self._user,
                password=self._password,
                database=self._database,
                port=self._port,
                charset='utf8mb4'
            )
        return self.connection

    # Đóng kết nối
    def close(self):
        if self.connection:
            self.connection.close()