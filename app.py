from flask import Flask, render_template, request
import mysql.connector
from datetime import date

app = Flask(__name__)

# --- DB CONNECTION ---
db = mysql.connector.connect(
    host="localhost",
    user="", #MySQL username here
    password="", #MySQL password here
    database="finance_app"
)

@app.route("/", methods=["GET", "POST"])
def index():
    page = request.args.get("page", "home")
    message = None
    success = False

    # ---------- ADD EXPENSE ----------
    if page == "add" and request.method == "POST":
        try:
            cursor = db.cursor()
            cursor.execute("""
                INSERT INTO transactions (date, type, person, amount, category, note)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                request.form["date"],
                request.form["type"],
                request.form["person"],
                request.form["amount"],
                request.form["category"],
                request.form["note"]
            ))
            db.commit()
            success = True
            message = "Transaction added successfully."
        except Exception as e:
            message = f"Error: {e}"

    # ---------- VIEW EXPENSES ----------
    results = None
    summary = None
    categories = None

    if page == "view" and request.method == "POST":
        from_date = request.form["from"]
        to_date = request.form["to"]

        cursor = db.cursor(dictionary=True)

        # Income / Expense suma
        cursor.execute("""
            SELECT type, SUM(amount) total
            FROM transactions
            WHERE date BETWEEN %s AND %s
            GROUP BY type
        """, (from_date, to_date))

        summary = {"income": 0, "expense": 0}
        for row in cursor.fetchall():
            summary[row["type"]] = row["total"]

        # Išlaidos pagal kategorijas
        cursor.execute("""
            SELECT category, SUM(amount) total
            FROM transactions
            WHERE type = 'expense'
              AND date BETWEEN %s AND %s
            GROUP BY category
            ORDER BY total DESC
        """, (from_date, to_date))

        categories = cursor.fetchall()
        results = True

    return render_template(
        "index.html",
        page=page,
        message=message,
        success=success,
        results=results,
        summary=summary,
        categories=categories,
        today=date.today().isoformat()
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

