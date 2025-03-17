from .get_csrf import get_csrf
from .get_ip import get_ip
from .uuid import uuid
from .cache import cache
from .markdown import markdown

# These are here so it's easier to remember. Just from utils import redirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
