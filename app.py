import os
from flask import Flask
from flask import render_template
from models import db
from api_v1 import api as api_v1

app = Flask(__name__)
app.register_blueprint(api_v1, url_prefix='/api/v1')

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/')
def hello():
    return 'hello World'

basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'nfgieqwognwngiwaogw'

db.init_app(app)
db.app = app

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)


with app.app_context():
    db.create_all()