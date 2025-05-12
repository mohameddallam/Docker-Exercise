import time
import redis
from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()  # Load env variables from .env

cache = redis.Redis(
    host=os.getenv('REDIS_HOST'),
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

@app.route('/titanic')  # ✅ Move it here!
def titanic():
    import pandas as pd
    df = pd.read_csv('static/titanic.csv')
    table_html = df.head().to_html(classes='data', header="true")

    survivors = df[df['Survived'] == 1]['Sex'].value_counts()
    genders = survivors.index.tolist()
    counts = survivors.values.tolist()

    return render_template('titanic.html', table=table_html, genders=genders, counts=counts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
