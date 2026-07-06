from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

# Database connection function
def get_connection():
    return pymysql.connect(
        host="ahad-mysql.cbikgkigc5pt.ap-south-1.rds.amazonaws.com",
        user="admin",
        password="ahad123456",
        database="company"
    )


@app.route("/", methods=["GET", "POST"])
def home():

    connection = get_connection()
    cursor = connection.cursor()

    # Form submit hone par
    if request.method == "POST":

        name = request.form["name"]
        salary = request.form["salary"]

        cursor.execute(
            "INSERT INTO employees (name, salary) VALUES (%s, %s)",
            (name, salary)
        )

        connection.commit()

    # Har request par employees fetch karo
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("index.html", employees=employees)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
