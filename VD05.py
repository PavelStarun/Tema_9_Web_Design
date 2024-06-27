from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def electric():
    return render_template('about.html')

@app.route('/dvs/')
def dvs():
    return render_template('home.html')

if __name__ == "__main__":
    app.run()
