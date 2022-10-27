from datetime import datetime
from bson import ObjectId
from flask import Flask, redirect, render_template
from pymongo import MongoClient
from flask import request

app = Flask(__name__)

# client = MongoClient("mongodb+srv://Idrees:idrees@mongodb-crud.irnsp.mongodb.net/test")
client = MongoClient("mongodb+srv://test:test@cluster0.vgzli.mongodb.net/test")
db = client["BotFusionAI_DB"]  # or db = client.test_database
collection = db["users"]  # or collection = db.test_collection$


#create function and route to add data
@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        data = {}
        data["_id"] = request.form["User_key"]
        data["userName"] = request.form["Username"]
        data["userMobile"] = request.form["mobile_number"]
        collection.insert_one(data)
        return redirect("/?_msg=User Created Successfully")
    else:
        return render_template("index.html")

#read the data
@app.route("/", methods=["GET"])
def main():
    msg = request.values.get("_msg")
    display = collection.find()
    display1 = collection.find()
    emp = list(display1)
    return render_template("main.html", collection=display, t=emp, text=msg)

#delete the data
@app.route("/delete")
def delete():
    key = request.values.get("_id")
    collection.delete_one({"_id": key})
    return redirect("/?_msg=User deleted Successfully")

#update the data
@app.route("/update", methods=["GET", "POST"])
def update():
    key = request.values.get("_id")
    user = collection.find_one({"_id": key})
    print(user)
    if request.method == "POST":
        updatedName = request.form["updated_username"]
        updatedMobile = request.form["updated_mobile"]
        collection.update_one({"_id": key}, {'$set': {"userName": updatedName, "userMobile": updatedMobile}})
        return redirect("/?_msg=User Updated Successfully")
    return render_template("update.html", user_id=key, data=user)

if __name__ == "__main__":
    app.run(debug=True)
