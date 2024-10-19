from functools import wraps
from django.shortcuts import redirect

def login_required_decorator(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('signin')  # Redirect to the sign-in page
        return view_func(request, *args, **kwargs)

    return _wrapped_view
