from flask import Flask, render_template, request

app = Flask(__name__)

def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()" for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        password = request.form["password"]
        result = check_strength(password)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)