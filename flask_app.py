from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def form():
    name = request.args.get ('name', ' ')
    if name == ' '
        return render_template('form.html')
    else 
        return ('Hello' + name )
