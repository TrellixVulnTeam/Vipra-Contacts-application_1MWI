from django.test import TestCase
import json
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Contact
from django.shortcuts import render, redirect,get_object_or_404
# Create your tests here.

class CreateContactTest(APITestCase):
    #Test to see if you can create a contact via a post request
    def test_create(self):
        data = {"name": "FakeName", "email":"test@testemail.com","Number":"01198765431"}
        response = self.client.post("http://127.0.0.1:8000/contacts/contacts-create/",data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response)

class DeleteContactTest(APITestCase):
    #Test to see if you can delete an entry that does not exist.
    def test_delete(self):
        response = self.client.post("http://127.0.0.1:8000/contacts/contacts-delete/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class ListContactsTest(APITestCase):

    def test_list_url(self):
        response = self.client.get("http://127.0.0.1:8000/contacts/contacts-list/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list(self):
        response = self.client.get("http://127.0.0.1:8000/contacts/contacts-list/")
        print(len(response.content))
        if len(response.content) == 2:
            pass
        else:
            self.fail("length does not match")