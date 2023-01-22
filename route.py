from passenger_wsgi import app
from flask import render_template, request, render_template, redirect, url_for, send_from_directory
from datetime import datetime
import forms

import data
import article_data


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
        "./home-page.html",
        current_title=data.homePage[country]['current_title'],
        content=data.homePage[country]['content'],
        topics=data.topic[country],
        current_country=country,
        btn_submit_form=data.homePage[country]['btn_submit_form'],
        alert_title=data.homePage[country]['alert_title'],
        email_placeholder=data.homePage[country]['email_placeholder'],
        description_placeholder=data.homePage[country]['description_placeholder'],
        nav=data.homePage[country]['nav_text'],
        disclaimer_link=url_for('disclaimer', country=country),
        disclaimer_title=data.homePage[country]['disclaimer_title'],
        copyright=data.homePage[country]['copyright'],
    )
    

@app.route('/<country>/about-page', methods=['GET'])
def about(country):
    return render_template(
        "./about-page.html",
        # markers=markers,
        current_title=data.aboutPage[country]['current_title'],
        content=data.aboutPage[country]['content'],
        current_country=country,
        nav=data.aboutPage[country]['nav_text'],
        disclaimer_link=url_for('disclaimer', country=country),
        disclaimer_title=data.homePage[country]['disclaimer_title'],
        copyright=data.homePage[country]['copyright'],
    )

@app.route('/<country>/contact-page', methods=['GET'])
def contact(country):
    articles1= list(filter(lambda article: article['most_asked'] == "true" , data.topicPage[country]['name1']['content']))
    articles2= list(filter(lambda article: article['most_asked'] == "true" , data.topicPage[country]['name2']['content']))
    articles3= list(filter(lambda article: article['most_asked'] == "true" , data.topicPage[country]['name3']['content']))
    articles4= list(filter(lambda article: article['most_asked'] == "true" , data.topicPage[country]['name4']['content']))
    articles5= list(filter(lambda article: article['most_asked'] == "true" , data.topicPage[country]['name5']['content']))

    articles = articles1 + articles2 + articles3 + articles4 + articles5
    return render_template(
        "./contact-page.html",
        current_title=data.contactPage[country]['current_title'],
        content=data.contactPage[country]['content'],
        current_country=country,
        nav=data.contactPage[country]['nav_text'],
        disclaimer_link=url_for('disclaimer', country=country),
        disclaimer_title=data.homePage[country]['disclaimer_title'],
        copyright=data.homePage[country]['copyright'],
        articles=articles,
        btn_submit_form=data.homePage[country]['btn_submit_form'],
        alert_title=data.homePage[country]['alert_title'],
        email_placeholder=data.homePage[country]['email_placeholder'],
        description_placeholder=data.homePage[country]['description_placeholder'],
    )

@app.route('/<country>/research-page', methods=['GET'])
def research(country):
    return render_template(
        "./research-page.html",
        current_title=data.researchPage[country]['current_title'],
        content=data.researchPage[country]['content'],
        current_country=country,
        nav=data.researchPage[country]['nav_text'],
        disclaimer_link=url_for('disclaimer', country=country),
        disclaimer_title=data.homePage[country]['disclaimer_title'],
        copyright=data.homePage[country]['copyright'],
    )

@app.route('/<country>/disclaimer-page', methods=['GET'])
def disclaimer(country):
    return render_template(
        "./disclaimer-page.html",
        current_title=data.disclaimerPage[country]['current_title'],
        content=data.disclaimerPage[country]['content'],
        current_country=country,
        nav=data.disclaimerPage[country]['nav_text'],
        disclaimer_link=url_for('disclaimer', country=country),
        disclaimer_title=data.homePage[country]['disclaimer_title'],
        copyright=data.homePage[country]['copyright'],
    )


@app.route('/<country>/topic/<topic_name>', methods=['GET'])
def topic(country, topic_name):
    return render_template(
        './topic-page.html',
        current_title=data.topicPage[country][topic_name]['current_title'],
        topics=data.topic[country],
        current_country=country,
        btn_submit_form=data.homePage[country]['btn_submit_form'],
        alert_title=data.homePage[country]['alert_title'],
        email_placeholder=data.homePage[country]['email_placeholder'],
        description_placeholder=data.homePage[country]['description_placeholder'],
        current_topic_name=topic_name,
        nav=data.disclaimerPage[country]['nav_text'],
        articles=data.topicPage[country][topic_name]['content'],
        disclaimer_link=url_for('disclaimer', country=country),
        disclaimer_title=data.homePage[country]['disclaimer_title'],
        copyright=data.homePage[country]['copyright'],
    )

@app.route('/<country>/topic/<topic_name>/<article_name>', methods=['GET'])
def article(country, topic_name, article_name):
    return render_template(
        './article-page.html',
        current_country=country,
        current_topic_name=topic_name,
        current_title=article_data.articlePage[country][article_name]['current_title'],
        nav=article_data.articlePage[country]['nav_text'],
        articles= article_data.articlePage[country][article_name]['content'],

        disclaimer_link=url_for('disclaimer', country=country),
        disclaimer_title=data.homePage[country]['disclaimer_title'],
        copyright=data.homePage[country]['copyright'],
    )