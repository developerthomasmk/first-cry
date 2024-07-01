from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == "" or password == "":
            flash("Please fill in all fields.")
        elif username == "admin" and password == "password":
            flash("Login successful!", "success")
        else:
            flash("Invalid username or password.", "danger")

    return render_template('./login.html')

if __name__ == '__main__':
    app.run(debug=True)
 