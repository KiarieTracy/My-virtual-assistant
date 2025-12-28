from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def intro():
    return render_template("intro.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    print(f"📩 Message from {name} ({email}): {message}")

    return render_template("index.html", success="Message sent successfully!")

if __name__ == "__main__":
    app.run()

