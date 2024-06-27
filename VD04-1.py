from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('VD03.html')

@app.route('/blog/')
def blog():
    return render_template('blog.html')

@app.route('/contacts/')
def contact():
    return render_template('contacts.html')

if __name__ == "__main__":
    app.run(debug=True)


