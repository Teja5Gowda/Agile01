from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data storage for simplicity (in-memory)
expenses = []
budget = 0

def calculate_financial_health():
    total_expenses = sum(expense['amount'] for expense in expenses)
    if budget == 0:
        return "Set a budget to monitor your financial health."
    elif total_expenses > budget:
        return f"You have exceeded your budget by ${total_expenses - budget:.2f}."
    else:
        return f"You are within budget. Remaining amount: ${budget - total_expenses:.2f}."

@app.route("/")
def index():
    financial_health = calculate_financial_health()
    return render_template("index.html", expenses=expenses, budget=budget, financial_health=financial_health)

@app.route("/add-expense", methods=["POST"])
def add_expense():
    name = request.form["expense-name"]
    amount = float(request.form["expense-amount"])
    expenses.append({"name": name, "amount": amount})
    return redirect(url_for("index"))

@app.route("/set-budget", methods=["POST"])
def set_budget():
    global budget
    budget = float(request.form["monthly-budget"])
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
