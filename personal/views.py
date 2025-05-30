from django.shortcuts import render

# Create your views here.
def home_screen_view(request):
	print(request.headers)
	return render(request,"base.html",{})
	
'''def products_view(request):
	print(request.headers)
	return render(request,"eShopping.html",{})'''

def eshopping(request):
    return render(request, "eshopping.html", {})




