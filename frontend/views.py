from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    """Home page view

    Args:
        request (GET): The request object

    Returns:    
        HTTPResponse: The rendered home page
    """
    
    context = {
        "title": "Home",
        "user": request.user,
    }
    return render(request, "frontend/index.html", context)