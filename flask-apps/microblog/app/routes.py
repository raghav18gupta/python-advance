from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    username = {'name': 'Raghav Gupta'}
    title = 'index page'
    return render_template('index.html', title='', user=username)
    # return render_template('index.html', title=title, user=username)


host, port, debug = '0.0.0.0', 5000, True
app.run(host, port, debug)
