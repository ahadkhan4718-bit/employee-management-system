from flask import Flask, render_template, request, redirect
from database import (
    add_employee,
    get_all_employees,
    search_employees,
    get_employee,
    update_employee,
    delete_employee, 
)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form["name"]
        salary = request.form["salary"]

        add_employee(name, salary)

        return redirect("/")

    keyword = request.args.get("search")

    if keyword:
        employees = search_employees(keyword)
    else:
        employees = get_all_employees()

    return render_template(
        "index.html",
        employees=employees
    )


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    if request.method == "POST":

        name = request.form["name"]
        salary = request.form["salary"]

        update_employee(id, name, salary)

        return redirect("/")

    employee = get_employee(id)

    return render_template(
        "edit.html",
        employee=employee
    )
@app.route("/delete/<int:id>")
def delete(id):

    delete_employee(id)

    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
