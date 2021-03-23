from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def form():
    name = request.args.get ('name', '')
    if name == '':
        return render_template('form.html')
    else:
        return 'Hello' + name 

@app.route('/write')
def write():
    f = open("demofile2.txt", "a")
    f.write("Now the file has more content!")
    f.close()
    f = open("demofile2.txt", "r")
    return 'file saved'

@app.route('/read')
def read():
    f = open("demofile3.txt", "w")
    return render_template('msg.html')
