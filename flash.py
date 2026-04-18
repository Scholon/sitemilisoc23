from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template("paginaprincipala.html")

@app.route('/user/<string:name>/<int:id>')
def user_id(name,id):
    return "Userul:" + name + " Numarul:" + str(id)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/milisoc")
def milisoc():
    return render_template("cevacreatdeclaudeai.html")

@app.route("/meniu")
def meniu():
    return render_template("meniu.html")

@app.route("/rezervare-masa")
def rezervaremasa():
    return render_template("rezervaremasa.html")

@app.route("/galerie")
def galerie():
    return render_template("galerie.html")





if __name__ == "__main__":
    app.run(debug=True, port= 4040)