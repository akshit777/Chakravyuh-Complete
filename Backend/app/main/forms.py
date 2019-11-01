from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField , PasswordField, SubmitField, ValidationError, TextAreaField,IntegerField,SelectField, FileField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Email,NumberRange
from .. import db
from ..models.users import User


class TeamRegistrationForm(FlaskForm):

    username = StringField('Name (Member 1)' , validators= [Length(3,50), DataRequired()])
    Roll_no1 = StringField('Roll Number (Member 1) ', validators = [Length(9), DataRequired()])
    email = StringField('Email (Member 1)', validators= [Email()])
    phone_number = StringField('Phone Number (Member 1)', validators = [Length(10), DataRequired()])
    Roll_no2 = StringField('Roll Number (Member 2) ', validators = [Length(9)])
    Submit = SubmitField('Register !')

class SoloRegistrationForm(FlaskForm):

    username = StringField('Name' , validators= [Length(3,50), DataRequired()])
    Roll_no1 = StringField('Roll Number', validators = [Length(9), DataRequired()])
    email = StringField('Email', validators= [Email()])
    phone_number = StringField('Phone Number', validators = [Length(10), DataRequired()])
    Submit = SubmitField('Register !')


    
    


        
        
    
    
    
