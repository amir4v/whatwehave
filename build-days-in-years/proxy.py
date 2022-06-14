import os
import sys
import inspect


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "whatwehave.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from days.models import *
