from django.test import TestCase
import datetime
from .models import Business, Neighbourhood, Post, Profile 
from django.contrib.auth.models import User


# Create your tests here.


class ProfileTest(TestCase):
    def setUp(self):
     
        self.user = User(username="nimoh", password="pass123")
        self.user.save()
        self.neighbourhood =  Neighbourhood(name = "Nairobi", location= "Rongai", admin = self.user,description='Good ambience', image="myhood.jpg" , health="720987564" , police="700099966")
        self.neighbourhood.save()
        self.profile = Profile(email='tests@gmail.com', profile_pic='profile.jpg', bio='living life',neighbourhood=self.neighbourhood,
                                    user=self.user)
      
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_delete_profile(self):
        self.profile.delete_profile()
        testsaved = Profile.objects.all()
        self.assertFalse(len(testsaved) > 0)

    def test_update_profile(self):
        self.profile.save_profile()
        self.profile.update_profile(self.profile.user_id)
        self.profile.save_profile()
        self.assertTrue(Profile,self.profile.user)


class NeighbourhoodTest(TestCase): 

    def setUp(self):
     
        self.user = User(username="nimoh", password="pass123")
        self.user.save()
        self.neighbourhood = Neighbourhood(name = "Nairobi", location= "Rongai", admin = self.user,description='Good ambience', image="myhood.jpg" , health="720987564" , police="700099966")
        self.neighbourhood.save()
   
    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,Neighbourhood))

    def test_save_hood(self):
        self.neighbourhood.save_hood()
        neighbourhood = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhood) > 0)

    def test_delete_hood(self):
        self.neighbourhood.delete_hood()
        testsaved = Neighbourhood.objects.all()
        self.assertFalse(len(testsaved) > 0)

    # def test_occupants_count(self):

class BusinessTest(TestCase): 

    def setUp(self):
     
        self.user = User(username="username", password="password")
        self.user.save()
        self.neighbourhood =  Neighbourhood(name = "Nairobi", location= "Rongai", admin = self.user,description='Good ambience', image="myhood.jpg" , health="720987564" , police="700099966")
        self.neighbourhood.save()
        self.business = Business(name="akantsy",user=self.user,email="testss@gmail.com", neighborhood=self.neighbourhood, description="Selling sneakers")
        self.business.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))

    def test_save_business(self):
        self.business.save_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

    def test_delete_hood(self):
        self.business.delete_business()
        business = Business.objects.all()
        self.assertFalse(len(business) > 0)


class PostTest(TestCase): 

    def setUp(self):
     
        self.user = User(username="nimoh", password="pass123")
        self.user.save()
        self.neighbourhood =  Neighbourhood(name = "Nairobi", location= "Rongai", admin = self.user,description='Good ambience', image="myhood.jpg" , health="720987564" , police="700099966")
        self.neighbourhood.save()
        self.post = Post(title="akanstry", post_image="tetsts.jpg" ,post_description ="my postss",user=self.user,neighbourhood=self.neighbourhood, date=datetime.datetime)
        self.post.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

    def test_save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Post.objects.all()
        self.assertFalse(len(post) > 0)
