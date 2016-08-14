#State the debug mode usage
DEBUG = True

#State the applicatoin directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "mysql://root:root@172.17.0.1/patients?charset=utf8"

THREADS_PER_PAGE = 2
CSRF_ENABLED = True


