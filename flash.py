from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template("new.html")

@app.route('/user/<string:name>/<int:id>')
def user_id(name,id):
    return "Userul:" + name + " Numarul:" + str(id)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/milisoc")
def milisoc():
    return render_template("cevacreatdeclaudeai.html")


if __name__ == "__main__":
    app.run(debug=True, port= 4040)