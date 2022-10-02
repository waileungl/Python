# from flask import Flask, render_template  # Import Flask to allow us to create our app
# app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# @app.route('/hello_world/<num>/<voca>')          # The "@" decorator associates this route with the function immediately following
# def hello_world(num, voca):
#     return render_template("test.html", number = int(num), vocab = voca)  # Return the string 'Hello World!' as a response

# @app.route('/dojo') 
# def dojo():
#     return 'Dojo!'

# @app.route('/say/<words>')
# def say(words):
#     return f"<div style='color:red'>Hi {str(words)}!</div>"

# @app.route('/repeat/<num>/<words>')
# def repeat(num, words):
#     result = ''
#     for i in range(0,int(num)):
#         result += f'<h1>{str(words)}</h1>'
#     return result

# @app.route('/<invalid>') 
# def alarm(invalid):
#     return 'Sorry! No response. Try again.'

# if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
#     app.run(debug=True)    # Run the app in debug mode.
alex = "w"

bob = ""

print(bob.join((f"hi{alex}","")))