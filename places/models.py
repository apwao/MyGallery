from django.db import models

class Location(models.Model):
    """
    Class Location to create instances of a location.
    In order to create an instance of a location, the location
    name is required
    """
    name = models.CharField(max_length = 80)
    description = models.TextField()
    
    def save_location(self):
        """
        save_location method to enable saving of an image's 
        location to the database
        """
        self.save()
        
    def delete_location(self):
        """
        delete_location method to remove a location from the database
        """
        self.delete()
        
    def edit_location(self):
        """
        edit_location method to change the name of a location in the database
        """
        self.update()
        
    def display_location(self):
        """
        display_location method to display all the locations saved in the database
        """
        self.get()
        
        

class Category(models.Model):
    """
    Class Category to create instances of a category.
    Requires the category name of the image
    """
    name = models.CharField(max_length=80)
    
    def save_category(self):
        """
        save_category method to enable saving of an image's 
        category to the database
        """
        self.save()
        
    def delete_category(self):
        """
        delete_category method to remove a category from the database
        """
        self.delete()
        
    def display_categories(self):
        """
        display_category method to display all the categories saved in the database
        """
        self.get()
        
    def edit_category(self):
        """
        display_category method to display all the categories saved in the database
        """
        self.get()
    
class tags(models.Model):
    """
    Tags class to create instances of tags for every image 
    to enable filtering of the images based on their tag names
    """
    name= models.CharField(max_length = 30)
    def save_tag(self):
        """
        save_tag method to enable saving of an image's tag
        to the database
        """
        self.save()
        
    def delete_tag(self):
        """
        delete_tag method to remove a tag from the database
        """
        self.delete()
        
    def edit_tag(self):
        """
        edit_tag method to replace an existing tag in the database
        with a different one
        """
        self.update()
        
    # def display_images(self):
    #     """
    #     display_images method to display all the images saved in the database
    #     """
    #     self.get()
      
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
        
    def save_image(self):
        """
        save_image method to enable saving of an image
        to the database
        """
        self.save()
        
    def delete_image(self):
        """
        delete_image method to remove an image from the database
        """
        self.delete()
        
    def edit_image(self):
        """
        edit_image method to replace an existing image in the database
        with a different one
        """
        self.update()
        
    def display_images(self):
        """
        display_images method to display all the images saved in the database
        """
        self.get()
        
    
