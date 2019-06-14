from django.db import models

class Location(models.Model):
    """
    Class Location to create instances of a location.
    In order to create an instance of a location, the location
    name is required
    """
    name = models.CharField(max_length = 80)
    description = models.TextField()

class Category(models.Model):
    """
    Class Category to create instances of a category.
    Requires the category name of the image
    """
    name = models.CharField(max_length=80)
    
class tags(models.Model):
    """
    Tags class to create instances of tags for every image 
    to enable filtering of the images based on their tag names
    """
    name= models.CharField(max_length = 30)
      
# Image Model
class Image(models.Model):
    """
    Class image to create instances of the image class. 
    To create an image instance that has the image name, description,
    location ForeignKey and Image category ForeignKey
    """
    image_name=models.CharField(max_length=60)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    tags=models.ManyToManyField(tags)
    pub_date=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        """
        Meta subclass to specify model-specific options
        such as the ordering format whenever the database is queried
        """
        ordering = ['id']
        
    
