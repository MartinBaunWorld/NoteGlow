import os
import geoip2.database


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
