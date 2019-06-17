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
    def tearDown(self):
        """
        tearDown method to create an clear the database after tests for each class are run
        """
        Location.objects.all().delete()
    
    def test_instance(self):
        """
        test_instance method to check for the correct creation of 
        an instance of Location
        """ 
        self.assertTrue(isinstance(self.santorini,Location))  
    
    def test_save_location(self):
        """
        test_save_location method to check whether an instance of loation
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
        locations=Location.objects.filter(name='Santorini').update(name='malibu')
        self.assertEquals(locations, 1)
        
    
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
    def tearDown(self):
        """
        tearDown method to create an clear the database after tests for each class are run
        """
        Category.objects.all().delete()

    def test_instance(self):
        """
        test_instance method to check for the correct creation of 
        an instance of Category
        """ 
        self.assertTrue(isinstance(self.adventure,Category))  
    
    def test_save_category(self):
        """
        test_save_category method to check whether an instance of category
        is successfully stored to the database
        """
        self.adventure.save_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)
    
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
        categories=Category.objects.all()
        self.assertTrue(len(categories)>1)
        
    def test_edit_category(self):
        """
        test_edit_category method to check whether it is possible
        to update a single category 
        """
        self.adventure.save_category()
        categories=Category.objects.filter(name="adventurous").update(name='adventure')
        self.assertEquals(categories, 1)
        
class TesttagsClass(TestCase):
    """
    class TesttagsClass to check for successful creation of 
    instances of tags
    """ 
    def setUp(self):
        """
        setUp method to create an instance of class tags to
        use during testing
        """
        self.adrenaline_junkie=tags(name='adrenaline_junkie')
    def tearDown(self):
        """
        tearDown method to create an clear the database after tests for each class are run
        """
        tags.objects.all().delete() 
    
    def test_instance(self):
        """
        test_instance method to check for the correct creation of 
        an instance of tags
        """ 
        self.assertTrue(isinstance(self.adrenaline_junkie,tags))
        
    def test_save_tag(self):
        """
        test_tag method to enable saving of a tag to the database
        """
        self.adrenaline_junkie.save_tag()
        tag=tags.objects.all()
        self.assertTrue(len(tag)>0)
        
    def test_delete_tag(self):
        """
        test_delete_tag to check whether an instance of tags
        is successfully deleted from the database once it has been stored
        """
        self.adrenaline_junkie.save_tag()
        self.adrenaline_junkie.delete_tag()
        tag=tags.objects.all()
        self.assertTrue(len(tag)<1)
        
    def test_display_tags(self):
        """
        test_display_tags method to check whether all the tags saved 
        in the database can be displayed
        """
        self.adrenaline_junkie.save_tag()
        tag2=tags(name='serenity')
        tag2.save_tag()
        tagies=tags.objects.all()
        self.assertTrue(len(tagies)>1)
        
    def test_edit_tags(self):
        """
        test_edit_tags method to check whether it is possible
        to update a single tags 
        """
        self.adrenaline_junkie.save_tag()
        tagies=tags.objects.filter(name='adrenaline_junkie').update(name='vicarious')
        self.assertEquals(tagies, 1)
        
            
          
class TestImageClass(TestCase):
    """
    Class TestImageClass to check for successful creation of
    image instances
    """
    def setUp(self):
        """
        setUp method to create an instance of image to
        use during testing
        """
        self.athens=Location(name='athens',description='the colosseum in Greece', id=1)
        self.architecture=tags(name='architecture', id=1)
        self.travel=Category(name='travel',id=1)
        self.unforgettable = Image(image_name='unforgettable',description='where the sky meets the earth',location=self.athens,category=self.travel,)
        # self.unforgettable.tags.add(self.architecture)
    def tearDown(self):
        """
        tearDown method to create an clear the database after tests for each class are run
        """
        Location.objects.all().delete()
        tags.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()
        
    
    def test_instance(self):
        """
        test_instance method to check for the correct creation of 
        an instance of tags
        """ 
        self.assertTrue(isinstance(self.unforgettable,Image))
        
    def test_save_image(self):
        """
        test_ave_image method to enable saving of an image all
        its details to the database
        """
        self.unforgettable.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)
        
    def test_delete_image(self):
        """
        test_delete_image to check whether an instance of image
        is successfully deleted from the database once it has been stored
        """
        self.unforgettable.save_image()
        self.unforgettable.delete_image()
        images=Image.objects.all()
        # self.assertTrue(len(images)<1)
        self.assertEquals(len(images), 0)
        
    def test_display_image(self):
        """
        test_display_image method to check whether all the images saved 
        in the database can be displayed
        """
        self.unforgettable.save_image()
        self.zanzibar=Location(name='zanzibar',description='the sandy beaches of Zanzibar')
        self.zanzibar.save_location()
        self.nature=tags(name='nature')
        self.nature.save_tag()
        self.outdoors=Category(name='outdoors')
        self.outdoors.save_category()
        self.outdoor_adventure = Image(image_name='outdoor_adventure',description='me and the deep blue sea',location=self.zanzibar,category=self.outdoors)
        self.outdoor_adventure.save_image()
        images2=Image.objects.all()
        self.assertTrue(len(images2)>1)
        
    def test_edit_image(self):
        """
        test_edit_image method to check whether it is possible
        to replace an existing image with a new one
        """
        self.unforgettable.save_image()
        images3=Image.objects.filter(image_name='unforgettable').update(image_name='divina')
        self.assertEquals(images3, 1)
        