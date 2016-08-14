#State the debug mode usage
DEBUG = True

#State the applicatoin directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root@/PATIENTS?unix_socket=/cloudsql/beautybee-139923:patients"

THREADS_PER_PAGE = 2
CSRF_ENABLED = True


