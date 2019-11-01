from flask import render_template, redirect, url_for, flash, redirect, current_app, abort
from . import main
from .forms import TeamRegistrationForm, SoloRegistrationForm
from .. import db
from ..models.users import User
from datetime import datetime
import os


@main.route('/BobTheBreaker/Register', methods=['GET', 'POST'])
def BobTheBreakerRegistration():
    form = TeamRegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data, phone_number = form.phone_number.data, Roll_no1=form.Roll_no1.data, Roll_no2=form.Roll_no2.data, event='BobTheBreaker')
        db.session.add(user)
        db.session.commit()
        flash('Registration Successful !')
        return render_template('BobTheBreaker.html')    
    return render_template('Register.html', form=form, event_name = 'Bob The Breaker')

@main.route('/CTF/Register', methods=['GET', 'POST'])
def CTFRegistration():
    form = TeamRegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data, phone_number = form.phone_number.data, Roll_no1=form.Roll_no1.data, Roll_no2=form.Roll_no2.data, event='CTF')
        db.session.add(user)
        db.session.commit()
        flash('Registration Successful !')
        return render_template('CTF.html')    
    return render_template('Register.html', form=form, event_name = 'CTF I_See_U')

@main.route('/PointOut/Register', methods=['GET', 'POST'])
def PointOutRegistration():
    form = SoloRegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data, phone_number = form.phone_number.data, Roll_no1=form.Roll_no1.data, Roll_no2=None, event='PointOut')
        db.session.add(user)
        db.session.commit()
        flash('Registration Successful !')
        return render_template('PointOut.html')    
    return render_template('Register.html', form=form, event_name = 'Point Out')

@main.route('/CodeEquity/Register', methods=['GET', 'POST'])
def CodeEquityRegistration():
    form = TeamRegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data, phone_number = form.phone_number.data, Roll_no1=form.Roll_no1.data, Roll_no2=form.Roll_no2.data, event='CodeEquity')
        db.session.add(user)
        db.session.commit()
        flash('Registration Successful !')
        return render_template('CodeEquity.html')    
    return render_template('Register.html', form=form, event_name = 'Code Equity')

@main.route('/CodeCeption/Register', methods=['GET', 'POST'])
def CodeCeptionRegistration():
    form = SoloRegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data, phone_number = form.phone_number.data, Roll_no1=form.Roll_no1.data, Roll_no2=None, event='CodeCeption')
        db.session.add(user)
        db.session.commit()
        flash('Registration Successful !')
        return render_template('CodeCeption.html')    
    return render_template('Register.html', form=form, event_name = 'Code Ception')

@main.route('/Hackathon/Register', methods=['GET', 'POST'])
def HackathonRegistration():
    return render_template('HackTU.html')

@main.route('/CodeRush/Register', methods=['GET', 'POST'])
def CodeRushRegistration():
    form = TeamRegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data, phone_number = form.phone_number.data, Roll_no1=form.Roll_no1.data, Roll_no2=form.Roll_no2.data, event='CodeRush')
        db.session.add(user)
        db.session.commit()
        flash('Registration Successful !')
        return render_template('CodeRush.html')    
    return render_template('Register.html', form=form, event_name = 'Code Rush')












