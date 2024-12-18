from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField,BooleanField,SelectField
from wtforms.validators import DataRequired, Length, EqualTo,ValidationError
from flask_wtf.file import FileAllowed
from .models.user import User


class RegistrationForm(FlaskForm):
    name = StringField("ФІО", validators=[DataRequired(), Length(min=2, max=100)])
    login = StringField("Логин", validators=[DataRequired(), Length(min=2, max=100)])
    password = PasswordField("Пароль", validators=[DataRequired()])
    confirm_password = PasswordField("Подтвердить Пароль", validators=[DataRequired(), EqualTo('password')])
    avatar = FileField("Загрузите фото", validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Зарегистрироватся')
    
    def validate_login(self, login):
        user = User.query.filter_by(login=login.data).first()
        if user:
            raise ValidationError('Виберете другой логин')
    


class LoginForm(FlaskForm):
    login = StringField("Логин", validators=[DataRequired(), Length(min=2, max=100)])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('войти')
    
    

class StudentForm(FlaskForm):
    student = SelectField('Student', choices=[], render_kw={'class': 'form-control'})
    
    
    
class TeacherForm(FlaskForm):
    student = SelectField('Student', choices=[], render_kw={'class': 'form-control'})