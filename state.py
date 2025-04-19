import os

import geoip2.database
from html_sanitizer import Sanitizer as _Sanitizer


def is_mergeable(a, b):
    return False

# TODO I have no idea what this exactly does
# I need to research this in depth for security
clean_html = _Sanitizer({
    'tags': {'p', 'br', 'b', 'i', 'strong', 'em', 'u', 'ul', 'ol', 'li', 'a', 'code', 'pre', 'h1', 'h2', 'h3', 'h4'},
    'attributes': {
        'a': {'href', 'title'},
    },
    'empty': {'p'}, 
    'separate': {'p'},
    'is_mergeable': is_mergeable,

}).sanitize

def clean_html2(body):
    return body


if os.path.exists(".ip.mmdb"):
    __geoip = geoip2.database.Reader(".ip.mmdb")
    def ip2country(ip):
        try:
            response = __geoip.country(ip)
            return response.country.names["en"]
        except geoip2.errors.GeoIP2Error:
            return "unknown"
else:
    print("Warning missing .geo.db, can't look up ips")
    def ip2country(ip):
        return "unknown"
