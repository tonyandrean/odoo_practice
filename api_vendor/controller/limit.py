import time
from odoo.http import request
from odoo.exceptions import AccessDenied

RATE_LIMIT = 10
TIME_WINDOW = 60

rate_limiter = {}

def is_rate_limited(ip):
    now = time.time()
    if ip not in rate_limiter:
        rate_limiter[ip] = []

    rate_limiter[ip] = [t for t in rate_limiter[ip] if now - t < TIME_WINDOW]

    if len(rate_limiter[ip]) >= RATE_LIMIT:
        return True

    rate_limiter[ip].append(now)
    return False

def rate_limit():
    ip = request.httprequest.remote_addr
    if is_rate_limited(ip):
        raise AccessDenied("Too many requests. Please try again later.")
