from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from reports.forms import ContactForm

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


def about(request):
    """About page view

    Args:
        request (GET): The request object

    Returns:    
        HTTPResponse: The rendered about page
    """
    
    context = {
        "title": "About",
        "user": request.user,
    }
    return render(request, "frontend/about.html", context)


def contact(request):
    """Contact page view
    Args:
        request (GET): The request object
    Returns:    
        HTTPResponse: The rendered contact page
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')
    else:
        form = ContactForm()
    
    return render(request, 'frontend/contact.html', {'form': form})

