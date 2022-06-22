from flask import request, render_template, session
from src.demo import app


@app.route('/', methods=['GET'])
def index():
    session.clear()
    session['name'] = 'PLACEHOLDER'
    return render_template('index.html', title='Index page')


@app.route('/playground', methods=['GET', 'POST'])
def playground():
    if request.method == 'POST':
        name = request.form['user_input']
        return render_template('playground.html', title='Playground page', name=name)
    else:
        try:
            name = session['name']
        except KeyError:
            name = 'PLACEHOLDER'
        return render_template('playground.html', title='Playground page', name=name)
