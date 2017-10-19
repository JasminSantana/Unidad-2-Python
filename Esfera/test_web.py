from esfera import sphere_volume
from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def home() -> '302':
    return redirect('/entry')


@app.route('/entry')
def go_entry() -> 'html':
    return render_template('entry.html', the_title='Welcome to the form')


@app.route('/calculate', methods=['POST'])
def calculate() -> 'html':
    r = float(request.form['r'])
    result = sphere_volume(r)
    title = "Sphere volume result"
    return render_template('result.html', the_r=r, the_result=result, the_title=title)


app.run(debug=True)
