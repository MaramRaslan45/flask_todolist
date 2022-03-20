import datetime
import json

from flask import Flask,render_template,request,redirect,url_for,jsonify
from forms import CreateForm,UpdateForm
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    create_refresh_token)

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret1234"

DATABASE_URI = "sqlite:///todo.db"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

db = SQLAlchemy(app)
jwt = JWTManager(app)


class Item (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String,nullable=False)
    description = db.Column(db.String,nullable=False)
    Deadline = db.Column(db.Date,default=datetime.date.today)

usernames = {'maram': 123, 'ahmed': 122,'khaled':111,'mohamed':123}
token=[]
@app.route('/', methods=['POST', 'GET'])
def home():
    items=Item.query.all()
    return render_template('home.html',items=items)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        print(username)
        password = request.form.get("password")
        if username in usernames:
            if usernames.get(username) == int(password):                access_token = create_access_token(identity=username)
                refresh_token = create_refresh_token(identity=username)
                token.append(access_token)
                return jsonify {
                    'status': 'success',
                    'data': {
                        'access_token': access_token,
                        'refresh_token': refresh_token
                    }
                }
        else:
            return render_template('login.html')

@app.route('/logout', methods=['GET'])
def logout():
    token.clear()
    return redirect(url_for('login'))


@app.route('/create',methods=['GET','POST'])
def create():
     form=CreateForm()

     if request.method == 'POST' and form.validate_on_submit():

        title=form.Title.data
        description=form.description.data
        deadline=form.dateofcompletion.data
        item=Item(title=title,description=description,Deadline=deadline)
        print(item)
        db.session.add(item)
        db.session.commit()

        return redirect(url_for('home'))

     else:
         return render_template('create.html',form=form)


@app.route('/update/<int:pk>',methods=['GET','POST'])
def update(pk):
    form = UpdateForm()
    item = Item.query.filter_by(id=pk)
    if request.method=='POST':
        title = form.Title.data
        description = form.description.data
        dl=form.dateofcompletion.data
        for i in item:
            i.title=title
            i.description=description
            i.Deadline=dl
        db.session.commit()

        return redirect(url_for('home'))

    else:
        return render_template('update.html', form=form,item=item)


@app.route('/delete/<int:pk>',methods=['GET','POST'])
def delete(pk):
    item=Item.query.filter_by(id=pk).first()
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/deleteall',methods=['GET','POST'])
def deleteall():
    items=Item.query.all()
    for i in items:
        db.session.delete(i)
    db.session.commit()
    return redirect(url_for('home'))



db.create_all()

app.run(debug=True)