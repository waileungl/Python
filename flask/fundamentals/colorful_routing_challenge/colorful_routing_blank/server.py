from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)


@app.route("/")
def index():
    print("Testing: Inside root route")
    return "Welcome to the colorful routes app!"

@app.route("/colors/<color>")
def show_color(color):

    print(f"Testing: The color is {color}")
    return color

@app.route("/colors/<color>/<number>")
def color_multiplier(color, number):
    print(f"Duplicating {color} {number} times...")

    return color * number

######### Predict the output #########

# What will show up in your terminal?
# What will show in your browser?
# Will there be an error and where do you think the error will show up?

# 1.) When you go to: localhost:5000
# 2.) When you go to: localhost:5000/colors/red
# 3.) When you go to: localhost:5000/colors/blue/8


######## Coding Challenge ########

# 4.) CODE: Fix the color_multiplier method so that it shows the color name as many times as the number.
# 5.) RESEARCH: For the color_multiplier function - How would you allow only integers to be passed through the number path variable?
# 6.) CODE: Add code to the show_color route, such that it will return a string that shows in your browser as an h2 tag with the background color matching that of the parameter. See the handout for the example. For this exercise do not create an actual html file/template.
# 7.) CODE:  Add that same background coloring to the color_multiplier route.
# 8.) CREATE: Add something extra all your own to the application. Points for comedy, creativity or ingenuity!


if __name__ == "__main__":
    app.run(debug=True)