# ----------------------------------------
# -- Flask => Intro and Your First Page --
# ----------------------------------------
# - Flask Is Micro Framework Built With Python
# --------------------------------------------
# - HTML
# - CSS
# - JavaScript
# --------------------------------------------

from flask import Flask, render_template

skills_app = Flask(__name__)


@skills_app.route("/")
def homepage():
    return render_template("HomePage.html")


@skills_app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    skills_app.run(debug=True, port=9000)
