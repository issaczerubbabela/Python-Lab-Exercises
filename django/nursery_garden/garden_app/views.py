from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Plant_Details

def plant_details(request):
	return render(request, 'insert.html')

def process_plant_details(request):
	if request.method=='POST':
		plant_name = request.POST.get('plant_name')
		plant_type = request.POST.get('plant_type')
		plant_price = request.POST.get('plant_price')
		plant_benefits = request.POST.get('plant_benefits')
		plant_detail = Plant_Details(plant_name=plant_name, plant_type=plant_type, plant_price=plant_price, plant_benefits=plant_benefits)
		plant_detail.save()

		return HttpResponse("Data successfully inserted!")
	else:
        	return HttpResponse("Invalid request method.")