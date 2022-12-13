from app import app
from flask import request
from model.model_response import model_class
obj = model_class()
@app.route("/user/put",methods=["PUT"])
def update_controller():
    return obj.update_mode_method(request.form)
@app.route("/user/delete/<id>",methods=["DELETE"])
def delete_controller(id):
    return obj.delete_mode_method(id)