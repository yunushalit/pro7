import os
from flask import Flask, request, render_template
from models.news import News
from models.news import News2
from models.news import News3
from models import db_session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandex'
db_session.global_init('db/sqlite.db')

@app.route('/')
@app.route('/hello')
@app.route('/hello/<name>')
def index(name='BAZA'):
    return render_template('index.html', name=name)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/baza')
def baza():
    session = db_session.create_session()
    return render_template(
        'base.html',
        news=session.query(News).order_by(News.date.desc()),
        news2=session.query(News2).order_by(News2.stazh.desc()),
        news3=session.query(News3).order_by(News3.zarplata.desc())
    )
    #return render_template('about.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

