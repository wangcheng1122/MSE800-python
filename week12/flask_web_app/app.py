from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/mySecondPage')
def mySecondPage():
    return render_template('mySecondPage.html')


@app.route('/username/<name>')
def learn(name):
    return f"{name} is learning Flask"


@app.route('/<name>/<int:number>')
def learn2(name, number):
    return f"{name} is learning Flask! He wakes up at {number} every day!"


@app.route('/mySecondPage/<age>')
def mySecondPage1(age):
    return render_template('mySecondPage.html', age=age)


if __name__ == '__main__':
    app.run(debug=True)
