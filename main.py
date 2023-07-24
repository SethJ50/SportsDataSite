""" from website import create_app

app = create_app()

if __name__ == '__main__': # only runs if you run this file directly
    app.run(debug=True) """

from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)


@app.route('/')
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs)

@app.route('/api/jobs')
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(debug=True)

