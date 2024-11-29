from flask import Flask, render_template

app = Flask(__name__)

#Função
@app.route("/")
def homepage():
    return render_template("homepage.html")


# coloca o site no ar
if __name__ == "__main__":
    app.run(debug=True)

print("Hello, world!!")
