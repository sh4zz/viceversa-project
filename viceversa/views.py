from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	test_get_text = request.GET['usertext']
	print(test_get_text)
	return render(request, 'reverse.html')