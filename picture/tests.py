from django.test import TestCase
from .models import Picture,Category,Location 

# Create your tests here.

class LocationTestClass(TestCase):
    #set up method
    def setUp(self):
        self.kenya=Location(location='Kenya')
    # To tear down instance
    def tearDown(self):
        Location.objects.all().delete()
    # Testing_instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kenya,Location))
    # Testing Save Method
    def test_save_method(self):
        self.kenya.save_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)>0)
    # Test Delete Method
    def test_delete_method(self):
        self.kenya.delete_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)==0)
    #Test get all method
    def test_get_all(self):
        self.kenya.get_all()
        locations=Location.objects.all()
        self.assertTrue(len(locations)==1)
    #Test update location method
    def test_update_location(self):
        self.kenya.save_location()
        self.kenya.update_location(self.kenya.id,'Iceland')
        iceland=Location.objects.get(location='Iceland')
        self.assertEqual(iceland.location,'Iceland')

class CategoryTestClass(TestCase):
    #set up method
    def setUp(self):
        self.food=Category(category='Food')
    # To tear down instance
    def tearDown(self):
        Category.objects.all().delete()
    # Testing_instance
    def test_instance(self):
        self.assertTrue(isinstance(self.food,Category))
    # Testing Save Method
    def test_save_method(self):
        self.food.save_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)
    #Test delete category method
    def test_delete_method(self):
        self.food.delete_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)==0)
    # Test get all categories method
    def test_get_all(self):
        self.food.get_all_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)==1)
    
    #Test update category
    def test_update_category(self):
        self.food.save_category()
        self.food.update_category(self.food.id,'Fashion')
        fashion=Category.objects.get(category='Fashion')
        self.assertEqual(fashion.category,'Fashion')

