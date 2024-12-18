import os

class Config(object):
    APPNAME = 'app'
    ROOT = os.path.abspath(APPNAME)
    UPLOAD_PATH = 'static/upload/'
    SERVER_PATH = os.path.join(ROOT, UPLOAD_PATH)
    

    USER= os.environ.get('POSTGRES_USER', 'admin')
    PASSWORD=os.environ.get('POSTGRES_PASSWORD', 'admin')
    HOST=os.environ.get('POSTGRES_HOST', '127.0.0.1')
    PORT=os.environ.get('POSTGRES_PORT', '5432')
    DB=os.environ.get('POSTGRES_DB', "new_db")


    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    SECRET_KEY = 'fosadlkdfm231i39123k1212312'
    SQLALCHEMY_TRACK_MODIFICATIONS = True




    #   SQLALCHEMY_DATABASE_URI = f"postgresql://admin:admin@localhost:5432/new_db"  # Исправлен URI базы данных
    #   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'  # Исправлен URI базы данных