from flask import redirect, request, session
from functools import wraps

class back(object):
    """To be used in views.

    Use `anchor` decorator to mark a view as a possible point of return.

    `url()` is the last saved url.

    Use `redirect` to return to the last return point visited.
    """

    default_view='public_views.home'
    
    @staticmethod
    def anchor(func):
        @wraps(func)
        def result(*args, **kwargs):
            session['back'] = request.url
            return func(*args, **kwargs)
        return result

    @staticmethod
    def url(default=default_view):
        anchor_point = session.get('back')
        if anchor_point:
            return anchor_point
        else:
            return default

    @staticmethod
    def redirect(default=default_view):
        return redirect(back.url(default))

back = back()
