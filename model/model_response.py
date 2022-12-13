import mysql.connector
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
            return "Update Suceesfull"
        else:
            return "Unsuccessful"

    def delete_mode_method(self,data):
        self.cur.execute(f"DELETE FROM user_info WHERE id = {data}")
        if self.cur.rowcount>0:
            return "delete Suceesfull"
        else:
            return "Unsuccessful"