import os
import django.template
from django.template import Template, loader, Context
from django.template.loader import get_template
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")

settings.configure(TEMPLATES=[{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [TEMPLATE_DIR]
}])

django.setup()
