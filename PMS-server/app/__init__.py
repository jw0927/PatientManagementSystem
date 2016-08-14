from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='./templates')
app.config.from_object('config')

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/Congratulation')
def hello():
    return render_template('404.html')

if __name__ == '__main__':
    app.run()

db.create_all()
