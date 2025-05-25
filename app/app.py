import os
import redis
import time
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()  # load .env locally (optional)

cache = redis.Redis(
    host=os.getenv('REDIS_HOST', 'srv-captain--redis'),
    port=6379,
    password=os.getenv('REDIS_PASSWORD')
)

app = Flask(__name__)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return render_template('hello.html', name="BIPM", count=count)

@app.route('/titanic')
def titanic():
    import pandas as pd
    df = pd.read_csv('static/titanic.csv')  # ensure static folder and file are lowercase and present
    table_html = df.head().to_html(classes='data', header="true")
    return render_template('titanic.html', table=table_html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)