import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

POSTGRESQL = {
    'default':{
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME':'qsistemas',
        'USER':'postgres',
        'PASSWORD':'password',
        'HOST':'localhost',
        'PORT':'5432',
    }
}

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}