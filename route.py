from passenger_wsgi import app
from flask import render_template, request, render_template, redirect, url_for
from datetime import datetime
import forms


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


#decorated function
@app.route('/')
@app.route('/landing-page')
def index():
    return render_template('landing-page.html', current_title='Landing page')


# Home page
############################################################
@app.route('/vn/home-page')
def homeVN():
    return render_template('/vn/home-page.html', current_title='Home page')
    

@app.route('/lao/home-page', methods=['GET', 'POST'])
def homeLao():
    return render_template('./laos/home-page.html', current_title='Home page')

@app.route('/cam/home-page', methods=['GET', 'POST'])
def homeCam():
    return render_template('./cambodia/home-page.html', current_title='Home page')

@app.route('/china/home-page', methods=['GET', 'POST'])
def homeChina():
    return render_template('./china/home-page.html', current_title='Home page')
############################################################


# About page
############################################################
@app.route('/vn/about-page')
def aboutVN():
    return render_template('/vn/about-page.html', current_title='About page')

@app.route('/lao/about-page', methods=['GET', 'POST'])
def aboutLao():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        print('Submitted title', form.title.data)
        return render_template('about-page.html', form=form, title=form.title.data)
    return render_template('about-page.html', current_title='About page', form=form)

@app.route('/cam/about-page', methods=['GET', 'POST'])
def aboutCam():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        print('Submitted title', form.title.data)
        return render_template('about-page.html', form=form, title=form.title.data)
    return render_template('about-page.html', current_title='About page', form=form)

@app.route('/china/about-page', methods=['GET', 'POST'])
def aboutChina():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        print('Submitted title', form.title.data)
        return render_template('about-page.html', form=form, title=form.title.data)
    return render_template('about-page.html', current_title='About page', form=form)
############################################################
