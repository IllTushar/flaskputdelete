import mysql.connector
import re
import jwt
from flask import make_response,request,json
from config.config import dbconfig
class auth_model():
    def __init__(self):
        try:
          self.con = mysql.connector.connect(host=dbconfig['hostname'],user=dbconfig['username'],password=dbconfig['password'],database=dbconfig['database'])
          self.con.autocommit=True
          self.cur = self.con.cursor(dictionary=True)
        except:
            print("Something went wrong")

    def auth_token(self,endpoint=""):
        def inner1(fun1):
            def inner2(*args):
                authorization=request.headers.get("authorization")
                if re.match("^Bearer *([^ ]+) *$",authorization,flags=0):
                    token = authorization.split(" ")[1]
                    endpoint = request.url_rule
                    print(endpoint)
                    try: 
                      jwtdecode = jwt.decode(token,"tushar",algorithms="HS256")
                    except jwt.ExpiredSignatureError:
                        return make_response({"message":"Token Expired"})
                    role_id =jwtdecode['payload']['role_info']
                    self.cur.execute(f"SELECT roles FROM accessibility_view WHERE endpoint = '{endpoint}'")
                    result = self.cur.fetchall()
                    if len(result)>0:
                        json_allowed = json.loads(result[0]['roles'])
                        if role_id in json_allowed:
                          return fun1(*args)
                        else:
                            return make_response({"message":"INVALID_ROLES"},404)
                else:
                    return make_response({"ERROR"})
            return inner2
        return inner1
