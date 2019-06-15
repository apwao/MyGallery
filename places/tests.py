from django.test import TestCase
from .models import Image,tags,Location,Category

# Create your tests here.

class LocationTestClass(TestCase):
    """
    Class ImageTestClass to test the functions of 
    """
    def setUp(self):
        """
        setUp method to create an instance of Location
        class to be used during testing
        """
        self.santorini=Location(name='Santorini',description='The warm sunny beaches of Greece')
    
    def test_instance(self):
        """
        test_instance method to check for the correct creation of 
        an instance of Location
        """ 
        self.assertTrue(isinstance(self.santorini,Location))  
    
    def test_save_method(self):
        """
        test_save_method to check whether an instance of loation
        is successfully stored to the database
        """
        self.santorini.save_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)>0)
        
    def test_delete_location(self):
        """
        test_delete_location to check whether an instance of location
        is successfully deleted from the database once it has been stored
        """
        self.santorini.save_location()
        self.santorini.delete_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)<1)
        
    def test_display_locations(self):
        """
        test_display_locations method to check whether all the locations saved 
        in the database can be displayed
        """
        self.santorini.save_location()
        location2=Location(name='cairo',description='the sandy dunes of the Arabian Desert')
        location2.save_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)>1)
        
    def test_edit_location(self):
        """
        test_edit_location method to check whether it is possible
        to update a single location 
        """
        self.santorini.save_location()
        locations=Location.objects.filter(id=1).update(name='malibu')
        self.assertEqual(locations.name, 'malibu')
    
class CategoryTestClass(TestCase):
    """
    class CategoryTestClass  to test the correct instantiation and functioning of the 
    Category class
    """
    def setUp(self):
        """
        setUp method to create an instance of Location
        class to be used during testing
        """
        self.adventure=Category(name='adventurous')
    
    def test_instance(self):
        """
        test_instance method to check for the correct creation of 
        an instance of Category
        """ 
        self.assertTrue(isinstance(self.adventure,Category))  
    
    def test_delete_category(self):
        """
        test_delete_category to check whether an instance of category
        is successfully deleted from the database once it has been stored
        """
        self.adventure.save_category()
        self.adventure.delete_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)<1)
        
    def test_display_categories(self):
        """
        test_display_categories method to check whether all the categories saved 
        in the database can be displayed
        """
        self.adventure.save_category()
        category2=Category(name='serenity')
        category2.save_category()
        categories=category2.objects.all()
        self.assertTrue(len(categories)>1)