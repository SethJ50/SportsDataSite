""" from website import create_app

app = create_app()

if __name__ == '__main__': # only runs if you run this file directly
    app.run(debug=True) """

from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': '$250,000'
    }, 
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Los Angeles, USA',
        'salary': '$300,000'
    },
    {
        'id': 3,
        'title': 'Front End Engineer',
        'location': 'Remote',
        'salary': '$100,000'
    },
    {
        'id': 4,
        'title': 'Back End Engineer',
        'location': 'Tucson, USA',
        'salary': '$120,000'
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)

