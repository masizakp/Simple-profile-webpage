"""
View functions for the personal app.

This module defines the view logic for rendering various pages such as
the homepage, shopping page, contact/order form, and custom informational pages.
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm


def home_screen_view(request):
    """
    Renders the home screen.

    Logs request headers for debugging and returns the base template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered base.html template.
    """
    print(request.headers)
    return render(request, "base.html", {})


def eshopping_view(request):
    """
    Renders the eShopping page.

    Logs request headers for debugging.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered eshopping.html template.
    """
    print(request.headers)
    return render(request, "eshopping.html", {})


def meetsetshehla_view(request):
    """
    Renders an informational extra page.

    Logs request headers for debugging.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered extrapage.html template.
    """
    print(request.headers)
    return render(request, "extrapage.html", {})


def order_view(request):
    """
    Handles the contact/order form submission.

    Processes form data on POST, saves valid data, and redirects to success page.
    Displays a blank form on GET.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered order.html with form, or redirect to success page.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'order.html', {'form': form})


def success_view(request):
    """
    Displays the success page after form submission.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered success.html template.
    """
    return render(request, 'success.html', {})


def polls_views(request):
    """
    Renders a page with links or embeds to polls-related content.

    Logs request headers for debugging.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered polls.html template.
    """
    print(request.headers)
    return render(request, "polls.html", {})
