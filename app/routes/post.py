from flask import  Blueprint, render_template,request,redirect
from ..extensions import db
from ..models.post import Post
from datetime import datetime
from flask_login import login_required
from ..forms import StudentForm, TeacherForm
from ..models.user import User
from flask_login import current_user

post = Blueprint('post', __name__)



@post.route('/', methods=['POST', 'GET'])
def all():
    posts = Post.query.order_by(Post.date.desc()).all()  # Сортування за спаданням
    return render_template('post/all.html', posts=posts, user=User)






@post.route('/post/create', methods=['POST', 'GET'])
@login_required
def create():
    form = StudentForm()
    form.student.choices = [s.name for s in User.query.filter_by(status="user")]
    if request.method == 'POST':
#        teacher = request.form.get('teacher')
        subject = request.form.get('subject')
        student = request.form.get('student')
        
        student_id = User.query.filter_by(name=student).first().id
        
        post = Post(teacher=current_user.id, subject=subject, student=student_id)
                
        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print (str(e))
        
        
        print(post.teacher)
        print(subject)
        print(student)
        return redirect('/')
    else:
        return render_template('post/create.html', form=form)
    
    
    
    
    
@post.route('/post/<int:id>/update', methods=['POST', 'GET'])
@login_required
def update(id):
    post = Post.query.get(id)
    if request.method == 'POST':
        post.teacher = request.form.get('teacher')
        post.subject = request.form.get('subject')
        post.student = request.form.get('student')
        
        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print (str(e))
    else:
        return render_template('post/update.html', post=post)
    
    
    
    
@post.route('/post/<int:id>/delete', methods=['POST', 'GET'])
@login_required
def delete(id):
    post = Post.query.get(id)
    try:
        db.session.delete(post)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        print (str(e))
        return  (str(e))
    
    
    
    


    












# @post.route('/post/<subject>')
# def create_post(subject):
#     post = Post(subject=subject)
#     db.session.add(post)
#     db.session.commit()
#     return 'You post is created'