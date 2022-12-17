import mysql.connector
from flask import make_response
from datetime import datetime,timedelta
import jwt
class model_class():
    def __init__(self):
        try:
          self.con  = mysql.connector.connect(host="localhost",user="root",password="",database="api_database")
          self.con.autocommit=True
          self.cur = self.con.cursor(dictionary=True)
        except:
            print("Something went wrong ")

    def update_mode_method(self,data):
        self.cur.execute(f"UPDATE user_info SET name='{data['name']}', email='{data['email']}', password='{data['password']}' WHERE id ='{data['id']}';")
        if self.cur.rowcount>0:
            return make_response({"message":"Update successful"},201)
        else:
            return make_response({"message":"Nothing to update"},202)

    def delete_mode_method(self,data):
        self.cur.execute(f"DELETE FROM user_info WHERE id = {data}")
        if self.cur.rowcount>0:
            return make_response({"message":"Deletion successful"},202)
        else:
            return make_response({"message":"Deletion unsccessful"},204)


    def get_all_data(self):
        self.cur.execute("SELECT * FROM user_info")
        result = self.cur.fetchall()
        if len(result)>0:
            return make_response({"data":result},200)
        else:
            return make_response({"message":"something went wrong"},204)


    def post_details(self,data):
        self.cur.execute(f"INSERT INTO user_info(id,name,email,password) VALUES('{data['id']}','{data['name']}','{data['email']}','{data['password']}');")
        return make_response({"message":"data uploaded"},200)

    def patch_the_data(self,data):
        qry="UPDATE user_info SET"
        for key in data:
            qry +=f" {key}='{data[key]}',"
        qry = qry[:-1]+f" WHERE id = {data['id']}"
        self.cur.execute(qry)
        if self.cur.rowcount>0:
            return make_response({"message":"updation successful"},201)
        else:
            return make_response({"message":"Nothing to update"},202)

    def pagination_all_data(self,limit,page):
        limit = int(limit)
        page = int(page)
        start = (limit*page)-limit
        self.cur.execute(f"SELECT * FROM user_info LIMIT  {start} ,{limit} ")
        result = self.cur.fetchall()
        if self.cur.rowcount>0:
            return make_response({"payload":result},200)
        else:
            return make_response({"message":"no record found"},204)

    def upload_images(self,uid,data):
        self.cur.execute(f"UPDATE user_info SET avatar='{data} where id = {uid}'")
        # result = self.cur.fetchall()
        if self.cur.rowcount>0:
            return make_response({"message":"update successfull"},201)
        else:
            return make_response({"message":"no data found"},202)

    def login_method(self,data):
        self.cur.execute(f"SELECT id,name,email,avatar, role_info FROM user_info where email='{data['email']}' and password = '{data['password']}'")
        result = self.cur.fetchall()
        user_data= result[0]
        exp_time1 = datetime.now() +timedelta(minutes=15)
        exp_epoch_time = int(exp_time1.timestamp())
        payload = {
            "payload":user_data,
            "exp":exp_epoch_time
        }
        token = jwt.encode(payload,"tushar",algorithm="HS256")
        return make_response({"token":token},200)
