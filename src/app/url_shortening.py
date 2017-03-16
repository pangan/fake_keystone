from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///url_shortening.db'

db = SQLAlchemy(app)


class ShortURL(db.Model):
    word = db.Column(db.String(4), primary_key=True)
    url = db.Column(db.Text)
    time_stamp = db.Column(db.TIMESTAMP)

    def __init__(self, word, url, time_stamp):
        self.word = word
        self.url = url
        self.time_stamp = time_stamp


@app.route('/')
def index():
    return 'URL Shortening!'


if __name__ == '__main__':
    db.create_all()
    app.run()