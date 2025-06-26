from flask import Flask, render_template, request
from phishing_rules import analyze_email
from password_strength import analyze_password

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/phishing', methods=['GET', 'POST'])
def phishing():
    result = ""
    issues = []
    if request.method == "POST":
        email_text = request.form["email"]
        result, issues = analyze_email(email_text)
    return render_template("phishing.html", result=result, issues=issues)

@app.route('/password', methods=['GET', 'POST'])
def password():
    result = ""
    issues = []
    if request.method == "POST":
        pwd = request.form["password"]
        result, issues = analyze_password(pwd)
    return render_template("password.html", result=result, issues=issues)


if __name__ == '__main__':
    app.run()