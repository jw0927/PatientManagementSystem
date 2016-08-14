#State the debug mode usage
DEBUG = True

#State the applicatoin directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost/patients?charset=utf8"

THREADS_PER_PAGE = 2
CSRF_ENABLED = True


