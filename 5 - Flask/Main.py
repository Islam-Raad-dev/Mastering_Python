# ----------------------------------------
# -------------- Flask -------------------
#-----------------------------------------

from flask import Flask, render_template

skills_app = Flask(__name__)


@skills_app.route("/")
def homepage():
    return render_template("HomePage.html",
                            pagetitle = "Home Page",
                            custom_css = "home")

@skills_app.route("/add")
def Abb():
    return render_template("add.html",
                            pagetitle="Add Skill",
                            custom_css="add")


@skills_app.route("/about")
def about():
    return render_template("about.html",
                            pagetitle = "About")


if __name__ == "__main__":
    skills_app.run(debug=True, port=9000)
