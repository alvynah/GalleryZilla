from django.test import TestCase
from .models import Picture,Category,Location 

# Create your tests here.

class LocationTestClass(TestCase):
    #set up method
    def setUp(self):
        self.kenya=Location(location='Kenya')
    # Testing_instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kenya,Location))
    # Testing Save Method
    def test_save_method(self):
        self.kenya.save_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)>0)
    def test_delete_method(self):
        self.kenya.delete_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)==0)

    def test_get_all(self):
        self.kenya.get_all()
        locations=Location.objects.all()
        self.assertTrue(len(locations)==1)
    def test_update_location(self):
        self.kenya.save_location()
        self.kenya.update_location(self.kenya.id,'Iceland')
        iceland=Location.objects.get(location='Iceland')
        self.assertEqual(iceland.location,'Iceland')
