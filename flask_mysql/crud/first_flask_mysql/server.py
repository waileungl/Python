from flask import Flask, render_template
# import the class from friend.py
from friend import Friend
app = Flask(__name__)
@app.route("/")
def index():
    myFriends = Friend.get_all()
    # call the get all classmethod to get all friends
    print(myFriends)
    return render_template("index.html", myFriends = myFriends)
            
if __name__ == "__main__":
    app.run(debug=True)