from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')

def index():
    data = {"name":"lucas","age":"19"}
    return render_template("index.html",mydata = data)

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
    name = "Lucas"
    return render_template("test.html",name = name)

@app.route('/sigupForm')
def sigupForm():
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    return render_template("get.html",data = {"name":fname,"lname":lname})

if __name__ == "__main__":
 app.run(debug=True)