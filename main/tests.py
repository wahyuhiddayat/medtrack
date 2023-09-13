from django.test import TestCase, Client
from .models import Item

class mainTest(TestCase):
    def setUp(self):
        self.data= Item.objects.create(
            name = "Paracetamol Tablets",
            price = 20000,
            amount = 20,
            category = "Medications",
            description = "Fever-reducing medicine containing 500mg of paracetamol per tablet.",

        ) 

    def test_product(self):
        self.assertEqual(self.data.name, "Paracetamol Tablets")
        self.assertEqual(self.data.price, 20000)
        self.assertEqual(self.data.amount, 20)
        self.assertEqual(self.data.category, "Medications")
        self.assertEqual(self.data.description, "Fever-reducing medicine containing 500mg of paracetamol per tablet.") 

    def setUp_web(self):
        self.client = Client()

    def test_template_elements(self):
        response = self.client.get('/main/') 

        self.assertEqual(response.status_code, 200) 

        self.assertContains(response, "<h1>Medtrack</h1>")
        self.assertContains(response, "<h5>Name: </h5>")
        self.assertContains(response, "<h4>Amount: </h4>")
        self.assertContains(response, "<h4>Price: </h4>")
        self.assertContains(response, "<h4>Category: </h4>")
        self.assertContains(response, "<h4>Description: </h4>")
 
        context = response.context  
        self.assertIn("name", context)
        self.assertIn("amount", context)
        self.assertIn("price", context)
        self.assertIn("category", context)
        self.assertIn("description", context)
