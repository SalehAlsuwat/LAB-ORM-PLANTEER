from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpRequest, HttpResponse
from .models import Plant, Review
# Create your views here.

def all_plants_view(request:HttpRequest):
    plants = Plant.objects.all()

    category = request.GET.get('category')
    edible = request.GET.get('is_edible')

    if category:
        plants = plants.filter(category = category)

    if edible == 'true':
        plants = plants.filter(is_edible = True)

    return render(request, 'plants/all.html', {'plants': plants})

def plant_detail_view(request: HttpRequest, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)

    related = Plant.objects.filter(
        category=plant.category
    ).exclude(id=plant_id)[0:3]

    reviews = Review.objects.filter(plant=plant)

    return render(request, 'plants/detail.html', {
        'plant': plant,
        'related': related,
        'reviews': reviews
    })
    
def add_plant_view(request:HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('name')
        about = request.POST.get('about')
        used_for = request.POST.get('used_for')
        category = request.POST.get('category')
        is_edible = request.POST.get('is_edible') == 'on'
        image = request.FILES.get('image')

        # Validation
        if not name or not about:
            return render(request, 'plants/form.html', {
                'error': 'Name and About are required!'
            })

        Plant.objects.create(
            name=name,
            about=about,
            used_for=used_for,
            category=category,
            is_edible=is_edible,
            image=image
        )

        return redirect('plants:all_plants_view')

    return render(request, 'plants/form.html')

def update_plant_view(request:HttpRequest, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)

    if request.method == 'POST':
        plant.name = request.POST.get('name')
        plant.about = request.POST.get('about')
        plant.used_for = request.POST.get('used_for')
        plant.category = request.POST.get('category')
        plant.is_edible = request.POST.get('is_edible') == 'on'

        if request.FILES.get('image'):
            plant.image = request.FILES.get('image')

        plant.save()
        return redirect('plant_detail', id=plant_id)

    return render(request, 'plants/form.html', {'plant': plant})

def delete_plant_view(request:HttpRequest, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)

    if request.method == 'POST':
        plant.delete()
        return redirect('plants:all_plants_view')

    return render(request, 'plants/delete.html', {'plant': plant})

def search_plant_view(request:HttpRequest):
    query = request.GET.get('q')
    results = []

    if query:
        results = Plant.objects.filter(name__icontains=query)

    return render(request, 'plants/search.html', {
        'results': results,
        'query': query
    })

def add_review_view(request:HttpRequest, plant_id):

    if request.method == "POST":
        plant_object = Plant.objects.get(id=plant_id)
        new_review = Review(plant=plant_object,name=request.POST["name"], comment=request.POST["comment"])
        new_review.save()

    return redirect("plant:plant_detail_view", id=plant_id)