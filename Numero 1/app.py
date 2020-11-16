from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/about',methods=['GET'])
def about():
    return render_template("home/apropos.html")


if __name__ == '__main__':
    app.run()
