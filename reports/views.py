"""Views for the waste management application."""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import GarbageReportForm
from .models import GarbageReport

# Create your views here.
def dashboard(request):
    """Render the dashboard page."""
    reports = GarbageReport.objects.all()

    if request.user.is_authenticated:
        user_reports = reports.filter(reported_by=request.user)
        print(user_reports)
    else:
        user_reports = None
    context = {
        'reports': user_reports,
    }
    return render(request, "reports/dashboard.html", context)

@login_required
def submit_report(request):
    if request.method == 'POST':
        form = GarbageReportForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            form.instance.reported_by = user
            report = form.save(commit=False)
            report.save()
            messages.success(request, 'Your garbage report has been submitted successfully!')
            return redirect('reports:dashboard')
    else:
        form = GarbageReportForm(initial={'name': request.user.first_name, 'email': request.user.email})
    
    return render(request, 'reports/submit_report.html', {'form': form})

def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def update_status(request, report_id):
    report = get_object_or_404(GarbageReport, pk=report_id)
    if report.status == 'Pending':
        report.status = 'Completed'
    else:
        report.status = 'Pending'
    report.save()
    messages.success(request, f'Report status updated to {report.status}')
    return redirect('reports:dashboard')

