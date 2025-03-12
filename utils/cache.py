from django.views.decorators.cache import cache_control as _cache_control


def cache(max_age=1, public=True):
    # TODO enable caching
    return _cache_control(max_age=0, public=public)
    return _cache_control(max_age=max_age*3600, public=public)
