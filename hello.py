from ensurepip import bootstrap
import os
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask_moment import Moment 
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import Form, StringField, SubmitField
from wtforms.validators import DataRequired 
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


# @app.route('/')
# def index():
#     user_agent = request.headers.get('user-Agent')
#     return '<p>Your browser is %s</p>' % user_agent

# @app.route('/')
# def index():
#     return '<h1> Bad Request</h1>', 400

# @app.route('/')
# def index():
#     return redirect('http://www.exampie.com')

# @app.route('/user/<id>')
# def get_user(id):
#     user = load_user(id)
#     if not user:
#         abort(404)
#     return '<h1>Hello , %s</h1>' % user.name


# @app.route('/index')
# def index():
#     return render_template('404.html')

# @app.route('/user/<name>')
# def user(name):
#     return render_template('user.html', name=name)

# @app.route('/')
# def index():
#     return render_template('index.html',current_time=datetime.utcnow())

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     name = None
#     form = NameForm()
#     if form.validate_on_submit():
#         name = form.name.data
#         form.name.data = ''
#     return render_template('index.html', form=form, name=name)

# @app.route('/', methods=['GET','POST'])
# def index():
#     form = NameForm()
#     if form.validate():
#         session['name'] = form.name.data
#         return redirect(url_for('index'))
#     return render_template('index.html', form=form, name=session.get('name'))
    
class Role(db.Model):
   __tablename__ = 'roles'
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(64), unique=True) 

   def __repr__(self):
      return '<Role %r>' % self.name
class User(db.Model):
   __tablename__ = 'users'
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(64), unique=True, index=True)

   def __repr__(self):
      return '<User %r>' % self.username

class Role(db.Model):
   users = db.relationship('User', backref='role')
class User(db.Model):
   role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     form = NameForm()
#     if form.validate_on_submit():
#         old_name = session.get('name')
#         if old_name is not None and old_name != form.name.data:
#            flash('Looks like you have changed your name!')
#         session['name'] = form.name.data
#         form.name.data = ''
#         return redirect(url_for('index'))
#     return render_template('index.html',form = form, name = session.get('name'))




# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404
 

# @app.route('/')
# def index():
#     response = make_response('<h1>This document carries a cookies!</h1>')
#     response.set_cookie('answer','42')
#     return response


# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)