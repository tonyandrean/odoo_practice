import time
from odoo.http import request
from odoo.exceptions import AccessDenied

RATE_LIMIT = 5
TIME_WINDOW = 60

rate_limiter = {}


def is_rate_limited(user_id):
    now = time.time()
    if user_id not in rate_limiter:
        rate_limiter[user_id] = []

    rate_limiter[user_id] = [t for t in rate_limiter[user_id] if now - t < TIME_WINDOW]

    if len(rate_limiter[user_id]) >= RATE_LIMIT:
        return True

    rate_limiter[user_id].append(now)
    return False

def rate_limit():
    user_id = request.env.user.id
    session_id = request.session.sid if request.session else None
    ip = request.httprequest.remote_addr

    identifier = f"{user_id}-{session_id}-{ip}"

    if is_rate_limited(identifier):
        raise AccessDenied("Too many requests. Please try again later.")
