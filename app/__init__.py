from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db=SQLAlchemy(app)

@app.errorhandelr(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/Congratulation')
def hello():
    return "Hello World For this Application!"

if __name__ == '__main__':
    app.run()