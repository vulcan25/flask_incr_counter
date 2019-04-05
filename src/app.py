import time

import redis
from flask import Flask, render_template, jsonify

# Set maximum counter id.  Stops user from submitting endless data to redis.
MAX_COUNTERS = 100

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count(counter_id):
    retries = 5
    while True:
        try:
            return cache.incr(str(counter_id) + ':hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
@app.route('/<int:counter_id>')
def hello(counter_id = None):
    if counter_id and 0 < counter_id <= MAX_COUNTERS:
        count = get_hit_count(counter_id)
        return jsonify ( {'result':'Hello World! counter {} has been clicked {} times.\n'.format(counter_id,count)})
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
