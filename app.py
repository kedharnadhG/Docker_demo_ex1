<<<<<<< HEAD
import time
from flask import Flask
app = Flask(__name__)
START = time.time()
def elapsed():
    running = time.time() - START
    minutes,seconds=divmod(running,60)
    hours,minutes=divmod(minutes,60)
    return "%d:%02d:%02d" % (hours,minutes,seconds)
@app.route("/")
def route():
    return "hello all (up %s)\n" % elapsed()
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
=======
import time
from flask import Flask
app = Flask(__name__)
START = time.time()
def elapsed():
    running = time.time() - START
    minutes,seconds=divmod(running,60)
    hours,minutes=divmod(minutes,60)
    return "%d:%02d:%02d" % (hours,minutes,seconds)
@app.route("/")
def route():
    return "hello all (up %s)\n" % elapsed()
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
>>>>>>> 986a026795a766a9caf13d8d4a013ea80895bed7
# http://127.0.0.1:8080/   (we can see the o/p in this site)