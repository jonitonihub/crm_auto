from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField,BooleanField,SelectField
from wtforms.validators import DataRequired, Length, EqualTo,ValidationError
from flask_wtf.file import FileAllowed
from .models.user import User


class RegistrationForm(FlaskForm):
    name = StringField("имя", validators=[DataRequired(), Length(min=2, max=100)])
    lastName = StringField("Фамілія", validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField("Логин", validators=[DataRequired(), Length(min=2, max=100)])
    password = PasswordField("Пароль", validators=[DataRequired()])
    repeatPassword = PasswordField("Подтвердить Пароль", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироватся')


class LoginForm(FlaskForm):
    login = StringField("Логин", validators=[DataRequired(), Length(min=2, max=100)])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('войти')
    
    

class StudentForm(FlaskForm):
    student = SelectField('Student', choices=[], render_kw={'class': 'form-control'})
    
    
    
class TeacherForm(FlaskForm):
    student = SelectField('Student', choices=[], render_kw={'class': 'form-control'})