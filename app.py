from flask import Flask, render_template, request, redirect
from database import add_employee, get_all_employees

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form["name"]
        salary = request.form["salary"]

        add_employee(name, salary)

        return redirect("/")

    employees = get_all_employees()

    return render_template(
        "index.html",
        employees=employees
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
