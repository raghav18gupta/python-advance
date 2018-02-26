
from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


host, port, debug = '0.0.0.0', 5000, True
app.run(host, port, debug)
