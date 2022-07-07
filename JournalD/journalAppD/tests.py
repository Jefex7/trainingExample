from datetime import timezone

from django.test import TestCase
import unittest
from django.test import Client

# Create your tests here.
from django.utils import dateformat
from django.urls import reverse
from journalAppD.forms import ResourceForm
from journalAppD.models import Resource


class TestJournal(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    def test_resources_page(self):
        # Issue a Get request.
        response = self.client.get('/resources')

        # Check that the response is 200 Ok
        self.assertEquals(response.status_code, 200)

    def test_resource_page(self):
        # Issue a Get request.
        response = self.client.get('/resource')

        # Check that the response is 200 Ok
        self.assertEquals(response.status_code, 200)

    def test_delete_page(self):
        # Issue a Get request.
        response = self.client.get('/delete_resource/#')

        # Check that the response is 200 Ok
        self.assertEquals(response.status_code, 200)

    def test_search_resource_page(self):
        # Issue a Get request.
        response = self.client.get('/search_resources')

        # Check that the response is 200 Ok
        self.assertEquals(response.status_code, 200)

    def test_resource_pdf_page(self):
        # Issue a Get request.
        response = self.client.get('/resources_pdf')

        # Check that the response is 200 Ok
        self.assertEquals(response.status_code, 200)

    def create_Resource(self, title="only a test", content="yes, this is only a test"):
        return Resource.objects.create(title=title, content=content)

    def test_resource_creation(self):
        w = self.create_Resource()
        self.assertTrue(isinstance(w, Resource))
        # self.assertEqual( w.title)

    # def test_whatever_list_view(self):
    #     w = self.create_Resource()
    #     url = reverse("journalAppD:view-resources")
    #     resp = self.client.get(b"url")
    #
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertIn(w.title, resp.content)


    # def test_valid_form(self):
    #     # formatted_date = dateformat.format(timezone.now, 'Y-m-d H:i')
    #     w = Resource.objects.create(self,title='Foo', content='Bar')
    #     data = {'title': w.title, 'content': w.content, }
    #     form = ResourceForm(data=data)
    #     self.assertTrue(form.is_valid())


    # def test_invalid_form(self):
    #     w = Resource.objects.create(title='Foo', content='')
    #     data = {'title': w.title, 'body': w.body, }
    #     form = ResourceForm(data=data)
    #     self.assertFalse(form.is_valid())
