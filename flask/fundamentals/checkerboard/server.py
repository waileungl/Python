from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def play():
    return render_template("checkerboard.html", x = 8, y = 8, color1 = "red", color2 = "black")

@app.route('/<int:x>')
def changeX(x):
    return render_template("checkerboard.html", x = x, y = 8, color1 = "red", color2 = "black")

@app.route('/<int:x>/<int:y>')
def changeXY(x,y):
    return render_template("checkerboard.html", x = x, y = y, color1 = "red", color2 = "black")

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def changeColor(x,y,color1, color2):
    return render_template("checkerboard.html", x = x, y = y, color1 = color1, color2 = color2)


if __name__=="__main__":
    app.run(debug=True) 