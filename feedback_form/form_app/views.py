from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FeedbackForm
from .models import Feedback


def home(request):
    reports = Feedback.objects.all().order_by('-created_at')
    selected_type = request.GET.get('damage_type')

    if selected_type:
        reports = reports.filter(damage_type=selected_type)

    return render(request, 'form_app/home.html', {
        'reports': reports,
        'selected_type': selected_type,
        'damage_types': Feedback.DAMAGE_TYPE_CHOICES,
    })


def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your property damage report was submitted!')
            return redirect('feedback_form')
    else:
        form = FeedbackForm()

    return render(request, 'form_app/feedback_form.html', {'form': form})