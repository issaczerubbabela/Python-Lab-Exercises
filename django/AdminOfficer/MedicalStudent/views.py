from django.shortcuts import render

# Create your views here.
def student_details(request):
	return render(request,'student_details.html')
	