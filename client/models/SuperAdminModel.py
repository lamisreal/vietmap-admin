from models.connectDB import ConnectDB
import hashlib

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
        super().__init__()
        
    def convertData(self, data):
        return [{"ID": row[0],
                 "USERNAME": row[1],
                 "EMAIL": row[2],
                 "ROLE": row[3],
                 "PASSWORD": row[4]
                 } for row in data]

    def login(self, USERNAME: str, password: str):
        db = self.connect()
        cursor = db.cursor()
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        query = "SELECT * FROM {0} WHERE USERNAME = %s AND ROLE = %s AND PASSWORD = %s".format(self.NAME_TABLE_SUPERADMIN)
        cursor.execute(query, (USERNAME, self.ROLE_SUPERADMIN, hashed_password))
        data = cursor.fetchall()
        self.close()
        return self.convertData(data)
    
    def get_data_by_id(self, USERNAME: str):
        db = self.connect()
        cursor = db.cursor()
        query = "SELECT * FROM {0} WHERE USERNAME = %s".format(self.NAME_TABLE_SUPERADMIN)
        cursor.execute(query, (USERNAME))
        data = cursor.fetchall()
        self.close()
        return self.convertData(data)
    
    def update(self, query):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        print(res)
        self.close()