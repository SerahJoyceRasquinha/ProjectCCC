from django.shortcuts import redirect
from functools import wraps

def login_required_decorator(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('signin')
        return view_func(request, *args, **kwargs)
    return wrapper
