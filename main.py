from flask import Flask
app =Flask(__name__)

@app.route("/")
def index():
    return "WOWWW nice"

@app.route("/hi")
def who():
    return "Congrats"

if __name__=="__main__":
    #app.run()
    app.run(host="127.0.0.1",port=8000,debug=True)