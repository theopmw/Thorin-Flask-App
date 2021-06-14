# Import os from standard Python library
import os
import json
# Import Flask class
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

# Create an instance of the Flask class and store it in a variable called app
# The first argument of the Flask class,
# is the name of the application's module - our package:
# (__name__)
# Since we're just using a single module,
# we can use __name__ which is a built-in Python variable
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


# app.route decorator (effectively, a decorator is a way of wrapping functions)
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
