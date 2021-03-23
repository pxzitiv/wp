from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def read():
    msg = request.args.get ('msg', '')
    if msg!='':
        f = open("file.txt", "w")
        f.write("msg")
        f.close()
    f = open("file.txt", "r")
    return f.read()

@app.route('/read')
def msg():
    return render_template('msg.html')
