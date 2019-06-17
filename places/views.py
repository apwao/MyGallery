from django.shortcuts import render
from .models import Category,Location,tags,Image
from django.http import HttpResponse, Http404

# Create your views here.

def home_page(request):
    """
    """
    # to_navbar()
    locations=Location.objects.all()
    images=Image.objects.all()
    categories = Category.objects.all()
    return render(request, 'my_places/home.html',{'images':images, 'locations':locations, 'categories':categories})   

def search_results(request):
    """
    search_results view function to query the database and
    return images associated with a given category
    """
    print(request)
    if 'category' in request.GET and request.GET['category']:
        
        search_term = request.GET.get('category')
        print(search_term)      
        searched_categories=Category.objects.filter(name=search_term)
        print(searched_categories)
        final_images=[]
        # all returns a querySet that can be iterated over to extract the category
        # search through the categories table for all categories whose name matches the search_term
        # obtaining the id of a single category in the returned querySet will reveal the id to be passed to the filter method
        # extracting the id of the category to be used in filtering in the image class
        for category in searched_categories:
            category_id = category.id
            print(category_id)
            # searching the db for all images bearing that specific id
            searched_images=Image.search_by_category(category_id)    
            print(searched_images)
            final_images.append(searched_images)        
                
        message=f'{search_term}'
        return render(request, 'my_places/search.html',{'message':message,'final_images':final_images})
    
    else:
        message='You have not searched anything'
        return render(request, 'my_places/search.html',{"message":message})

# def display_by_location():
#     """
#     display_by_location 
#     """
#     locations=Location.objects.all()
#     return locations
    
# def display_images_by_location():
#     """
#     """
#     place_images=Image.objects.all()
#     return place_images

def view_by_location(request):
    """
    """
    locations=Location.objects.all()
    images=Image.filter_by_location()
    
    return render(request, 'my_places/location.html',{'images':images,'locations':locations})

# def single_image(request):
    

# def to_navbar():
#     """
#     """
#     nav_locations=[]
#     nav_categories=[]
#     all_locations=Location.objects.all()
#     all_categories = Category.objects.all()
    
#     for location in all_locations:
#         if location.name not in all_locations:
#             nav_locations.append(location.name)
            
#     for category in all_categories:
#         if category.name not in all_categories:
#             nav_categories.append(category.name)
            
#     return render('my_places/navbar.html',{'nav_locations':nav_locations, 'nav_categories':nav_categories})