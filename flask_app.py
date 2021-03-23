from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def msg():
    msg = request.args.get ('msg', '')
    f = open("demofile2.txt", "a")
    f.write("Now the file has more content!")
    f.close()
    f = open("demofile2.txt", "r")
    return render_template('msg.html')

@app.route('/read')
def read():
    f = open("demofile3.txt", "w")
    return render_template('msg.html')
