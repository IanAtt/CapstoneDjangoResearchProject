# form_app/views.py
from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.contrib import messages

def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your feedback!')
            return redirect('feedback_form') # Redirect to the same page
    else:
        form = FeedbackForm()
    return render(request, 'form_app/feedback_form.html', {'form': form})