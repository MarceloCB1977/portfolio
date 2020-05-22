from secret import dbname, host, passwd, username

DEBUG = True

SQLALCHEMY_DATABASE_URI = f'postgres://{username}:{passwd}@{host}/{dbname}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'supersecretkey'
