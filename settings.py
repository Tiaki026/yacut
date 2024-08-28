import os
from string import ascii_letters, digits


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')


CHAR_POOL = ascii_letters + digits
BASE_URL = 'http://localhost/'
INDEX = 'index.html'
URL_ALLREADY_EXIST = 'Предложенный вариант короткой ссылки уже существует.'
WRONG_NAME_SHORT_URL = 'Указано недопустимое имя для короткой ссылки'
WITHOUT_BODY = 'Отсутствует тело запроса'
WRONG_ID = 'Указанный id не найден'
REQUIRED_FIELD = '"url" является обязательным полем!'
SHORT_LENGTH_URL = 16
LONG_LENGHT_URL = 256
