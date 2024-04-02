from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    counter = str(redis.get('hits'),'utf-8')
    return "<html><head><h2 style='color:#00008B;text-align:center'> This is the  <span style='color:red'>" + counter + "</span> Visitor.</h2></body></html>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
