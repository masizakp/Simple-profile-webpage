from django.shortcuts import render

# View function for the eShopping page
def eshopping(request):
    # Logs the request headers to the console (for debugging purposes)
    print(request.headers)
    # Renders the 'eShopping.html' template without any context data
    return render(request, "eShopping.html", {})
