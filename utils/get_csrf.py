from django.middleware.csrf import get_token


def get_csrf(request):
    return f'<input type="hidden" name="csrfmiddlewaretoken" value="{get_token(request)}">'
