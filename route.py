from passenger_wsgi import app
from flask import render_template, request, render_template, redirect, url_for, send_from_directory
from datetime import datetime
import forms

import data


@app.context_processor
def inject_now(): return {'now': datetime.utcnow()}

@app.route('/favicon.ico') 
def favicon(): return send_from_directory('static/icon', 'favicon.ico', as_attachment=True)

@app.route('/')
def redirectIndex(): return redirect(url_for('index'))

@app.route('/landing-page')
def index(): return render_template('landing-page.html', current_title='Landing page')

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

@app.route('/<country>', methods=['GET'])
def redirectHome(country): return redirect(url_for('home', country=country))

@app.route('/<country>/home-page', methods=['GET'])
def home(country):
    return render_template(
        data.homePage[country]['template'],
        current_title=data.homePage[country]['current_title'],
        content=data.homePage[country]['content'],
        topics=data.topic[country],
        home_link=url_for('home', country=country),
        about_link=url_for('about', country=country),
        contact_link=url_for('contact', country=country),
        research_link=url_for('research', country=country),
        disclaimer_link=url_for('disclaimer', country=country),
    )
    

@app.route('/<country>/about-page', methods=['GET'])
def about(country):
    return render_template(
        data.aboutPage[country]['template'],
        current_title=data.aboutPage[country]['current_title'],
        content=data.aboutPage[country]['content'],
        home_link=url_for('home', country=country),
        about_link=url_for('about', country=country),
        contact_link=url_for('contact', country=country),
        research_link=url_for('research', country=country),
        disclaimer_link=url_for('disclaimer', country=country),
    )

@app.route('/<country>/contact-page', methods=['GET'])
def contact(country):
    return render_template(
        data.contactPage[country]['template'],
        current_title=data.contactPage[country]['current_title'],
        content=data.contactPage[country]['content'],
        home_link=url_for('home', country=country),
        about_link=url_for('about', country=country),
        contact_link=url_for('contact', country=country),
        research_link=url_for('research', country=country),
        disclaimer_link=url_for('disclaimer', country=country),
    )

@app.route('/<country>/research-page', methods=['GET'])
def research(country):
    return render_template(
        data.researchPage[country]['template'],
        current_title=data.researchPage[country]['current_title'],
        content=data.researchPage[country]['content'],
        home_link=url_for('home', country=country),
        about_link=url_for('about', country=country),
        contact_link=url_for('contact', country=country),
        research_link=url_for('research', country=country),
        disclaimer_link=url_for('disclaimer', country=country),
    )

@app.route('/<country>/disclaimer-page', methods=['GET'])
def disclaimer(country):
    return render_template(
        data.disclaimerPage[country]['template'],
        current_title=data.disclaimerPage[country]['current_title'],
        content=data.disclaimerPage[country]['content'],
        home_link=url_for('home', country=country),
        about_link=url_for('about', country=country),
        contact_link=url_for('contact', country=country),
        research_link=url_for('research', country=country),
        disclaimer_link=url_for('disclaimer', country=country),
    )


@app.route('/<country>/topic/<topic_name>', methods=['GET'])
def topic(country, topic_name):
    return render_template(
        data.topicPage[country][topic_name]['template'],
        current_title=data.topicPage[country][topic_name]['current_title'],
        content=data.topicPage[country][topic_name]['content'],
        topics=data.topic[country],
        home_link=url_for('home', country=country),
        about_link=url_for('about', country=country),
        contact_link=url_for('contact', country=country),
        research_link=url_for('research', country=country),
        disclaimer_link=url_for('disclaimer', country=country),
    )