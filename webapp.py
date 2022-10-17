from unicodedata import name
from flask import Flask,render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
app = Flask(__name__)
app.config ['SECRET_KEY'] = 'mykey'

class Myform(FlaskForm):
    name = StringField('ใส่ชื่อ')
    submit = SubmitField("บันทึก")


@app.route('/',methods =['get','post'])
def index():
    name = False 
    form = Myform()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
    return render_template('index.html', form = form,name = name)

@app.route('/shop')
def shop():
    name = ["cat","dog","lucas","x","b","god"]
    return render_template("shop.html",mp = name )

@app.route('/admin')
def admin():
    name = "Lucas"
    return render_template("admin.html",name = name)


@app.route('/test')
def testweb():
    name = Myform()
    return render_template("test.html",form = name)

@app.route('/sigupForm')
def sigupForm():
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    return render_template("get.html",data = {"name":fname,"lname":lname})

@app.route('/sandbox')
def sandbox():
    name = "Lucas"
    return render_template("sandbox.html",name = name)

@app.route('/urlsand')
def testlink():
    namel = request.args.get('name1')
    namell = request.args.get('sand')
    return render_template("show.html",d = {"name":namel,"namell":namell})

if __name__ == "__main__":
 app.run(debug=True)