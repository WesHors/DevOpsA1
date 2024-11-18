## Test 1 Route Test

## This test verifies that the application correctly handles invalid HTTP methods for a specific route. By sending POST requests to the / route.

import unittest
from app import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_invalid_method(self):
        """Test that an invalid request method returns 405."""
        response = self.client.post('/')
        self.assertEqual(response.status_code, 405)

if __name__ == '__main__':
    unittest.main()

## Test 2 DB Read Test

## This test checks the database connection using Mongo's ping command, ensures the connection is maintained.
 

import unittest
from pymongo import MongoClient
import os

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient(os.getenv('MONGODB_URI'))
        self.db = self.client.get_database("shop_db")

    def test_ping(self):
        """Test the database connection using a ping command."""
        self.assertTrue(self.client.admin.command('ping'))

if __name__ == '__main__':
    unittest.main()


## Test 3 DB Write Test

## Confirms that the DB can do Write actions by inserting a test document into the products collection. Checks for valid ID as confirmation.

import unittest
from pymongo import MongoClient
import os

class TestDatabaseWrite(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient(os.getenv('MONGODB_URI'))
        self.db = self.client.get_database("shop_db")
        self.collection = self.db.get_collection("products")

    def test_insert_document(self):
        """Test inserting a document into the products collection."""
        test_doc = {"name": "Test Product", "tag": "test", "price": 1.99, "image_path": "static/images/test.jpg"}
        result = self.collection.insert_one(test_doc)
        self.assertIsNotNone(result.inserted_id)
        self.collection.delete_one({"_id": result.inserted_id})

if __name__ == '__main__':
    unittest.main()
