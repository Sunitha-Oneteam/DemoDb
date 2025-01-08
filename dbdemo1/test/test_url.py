from django.test import SimpleTestCase
from django.urls import reverse,resolve
from dbdemo1.views import home

class TestUrl(SimpleTestCase):

    def test_home(self):
        #assert 1==2 
        url=reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func,home)