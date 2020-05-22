from django.shortcuts import render, redirect
from app.views import *
from .forms import ReviewRequestForm

def newReview(request):
    if request.method == "POST":
        form = ReviewRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = ReviewRequestForm()

    return render(request, "reviews/newreview.html", {"form": form })
