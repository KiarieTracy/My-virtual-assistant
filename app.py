from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"📩 New message from {name} ({email}): {message}")
        return render_template("index.html", success="Message sent successfully!")
    else:
        return render_template("index.html", success="Opened contact page via GET request.")


if __name__ == "__main__":
    app.run()
