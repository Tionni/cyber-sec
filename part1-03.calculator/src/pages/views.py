from django.http import HttpResponse


# Create your views here.

def addPageView(request):
	first = request.GET.get('first')
	second = request.GET.get('second')
	sum = int(first) + int(second)
	return HttpResponse(sum)
	

def multiplyPageView(request):
	first = request.GET.get('first')
	second = request.GET.get('second')
	mult = int(first) * int(second)
	return HttpResponse(mult)
