import mysql.connector
import re
import jwt
from flask import make_response,request
class auth_model():
    def __init__(self):
        try:
          self.cur = mysql.connector.connect(host="localhost",user="root",password="",database="api_database")
          self.cur.autocommit=True
          self.con = self.cur.cursor(dictionary=True)
        except:
            print("Something went wrong")

    def auth_token(self,endpoint):
        def inner1(fun1):
            def inner2(*args):
                authorization=request.headers.get("authorization")
                if re.match("^Bearer *([^ ]+) *$",authorization,flags=0):
                    token = authorization.split(" ")[1]
                    print(token)
                    return fun1(*args)
                else:
                    return make_response({"ERROR"})
            return inner2
        return inner1
