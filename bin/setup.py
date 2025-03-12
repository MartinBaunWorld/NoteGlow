import sys
import os
import django

# Set up .. as path as well
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/..') # noqa

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()
