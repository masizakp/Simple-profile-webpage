from django.shortcuts import render

# View function for the home screen
def home_screen_view(request):
    # Logs the request headers to the console (for debugging purposes)
    print(request.headers)
    # Renders the 'base.html' template without any context data
    return render(request, "base.html", {})
