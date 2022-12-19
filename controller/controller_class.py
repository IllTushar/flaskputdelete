from app import app
from flask import request
from model.model_response import model_class
from model.auth_model import auth_model
from datetime import datetime
obj = model_class()
auth = auth_model()
@app.route("/user/put",methods=["PUT"])
def update_controller():
    return obj.update_mode_method(request.form)
@app.route("/user/delete/<id>",methods=["DELETE"])
def delete_controller(id):
    return obj.delete_mode_method(id)
    
@app.route("/user/getall")
@auth.auth_token()
def get_all_details():
    return obj.get_all_data()
@app.route("/user/post",methods=["POST"])
def get_post_data():
    return obj.post_details(request.form)

@app.route("/user/addmultiple",methods=["POST"])
def add_multiple_data():
    return obj.post_multiple_row(request.json)
@app.route("/user/patch",methods=["PATCH"])
def patch_data():
    return obj.patch_the_data(request.form)
@app.route("/user/getall/limit/<limit>/page/<page>")
def get_all_limit_data(limit,page):
    return obj.pagination_all_data(limit,page)
@app.route("/user/<uid>/upload/avatar",methods=["PUT"])
def user_upload_avatar_control(uid):
     file  = request.files['avatar']
     uniqueFileName = str(datetime.now().timestamp()).replace(".", "")
     fileNameSplit = file.filename.split(".")
     ext = fileNameSplit[len(fileNameSplit)-1]
     finalPath = f"upload/{uniqueFileName}.{ext}"
     file.save(finalPath)
     return obj.upload_images(uid,finalPath)

@app.route("/user/login",methods=["POST"])
def login_request():
    return obj.login_method(request.form) 