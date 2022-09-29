from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    # block = "<div></div>"
    return render_template("playground.html", num = 1 , color = "seagreen")

@app.route('/play/<int:num>')
def block(num):
    block = "<div></div>"
    return render_template("playground.html", num = num, block = block, color = "seagreen")

@app.route('/play/<int:num>/<color>')
def colorBlock(num, color):
    block = "<div></div>"
    return render_template("playground.html", num = num,block = block, color = color)



if __name__=="__main__":
    app.run(debug=True) 