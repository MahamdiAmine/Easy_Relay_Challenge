import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Product, Client, Order
from .serializers import ProductSerializer, ClientSerializer, OrderSerializer

PRODUCTS_URL = reverse("product-list")
PRODUCT_DETAIL = "product-detail"

CLIENTS_URL = reverse("client-list")
CLIENT_DETAIL = "client-detail"

ORDERS_URL = reverse("order-list")
ORDER_DETAIL = "order-detail"


# products
class ProductApiTest(TestCase):
    """
    test the Product
    """

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_products_list(self):
        # Test retrieving a list of products
        Product.objects.create(
            code="PR001",
            name="Product 1",
            family="F001",
            price=137,
        )
        Product.objects.create(
            code="PR002",
            name="Product 2",
            family="F001",
            price=200,
        )
        response = self.client.get(PRODUCTS_URL)
        products = Product.objects.all().order_by("id")
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_product(self):
        # test creating a new product
        product = {
            "code": "PR003",
            "name": "Product 3",
            "family": "F002",
            "price": 1500,
            "remark": "test creating a new product"
        }
        self.client.post(PRODUCTS_URL, product)
        exists = Product.objects.filter(code=product["code"]).exists()
        self.assertTrue(exists)


class GetSingleProductTest(TestCase):
    """
     Test module for GET single product API
    """

    def setUp(self):
        self.client = APIClient()

    def test_get_valid_single_product(self):
        product4 = Product.objects.create(
            code="PR004",
            name="Product 4",
            family="F002",
            price=185,
            remark="test retrieving a product"
        )
        response = self.client.get(
            reverse(PRODUCT_DETAIL, kwargs={"pk": product4.pk})
        )
        serializer = ProductSerializer(product4)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_product(self):
        response = self.client.get(
            reverse(PRODUCT_DETAIL, kwargs={"pk": 6})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UpdateSingleProductTest(TestCase):
    """
     Test module for updating an existing product record
     """

    def setUp(self):
        self.client = APIClient()

    def test_valid_update_product(self):
        product5 = Product.objects.create(
            code="PR005",
            name="Product 5",
            family="F002",
            price=300,
        )
        updated_product5 = {
            "code": "PR005",
            "name": "Updated Product 5",
            "family": "F005",
            "price": 265,
        }
        response = self.client.put(
            reverse(PRODUCT_DETAIL, kwargs={"pk": product5.pk}),
            data=json.dumps(updated_product5),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_product(self):
        invalid_update_product6 = {
            "code": "PR006",
            "remark": "invalid Updated for Product 6",
            "price": 100
        }
        product6 = Product.objects.create(
            code="PR006",
            name="Product 6",
            family="F002",
            price=270,
        )
        response = self.client.put(
            reverse(PRODUCT_DETAIL, kwargs={"pk": product6.pk}),
            data=json.dumps(invalid_update_product6),
            content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleProductTest(TestCase):
    """
    Test module for deleting an existing product record
    """

    def setUp(self):
        self.client = APIClient()

    def test_valid_delete_product(self):
        product6 = Product.objects.create(
            code="PR006",
            name="Product 6",
            family="F003",
            price=330,
        )
        response = self.client.delete(
            reverse(PRODUCT_DETAIL, kwargs={"pk": product6.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_product(self):
        response = self.client.delete(
            reverse(PRODUCT_DETAIL, kwargs={"pk": 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


# clients
class ClientApiTest(TestCase):
    """
    test the Client
    """

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_clients_list(self):
        # Test retrieving a list of clients
        Client.objects.create(
            code="CL001",
            first_name="client1",
            last_name="client1",
            address="Batna, Algeria",
            date_of_birth="1990-01-01",
            mobile_phone1="0123456789",
        )
        Client.objects.create(
            code="CL002",
            first_name="client2",
            last_name="client2",
            address="Batna, Algeria",
            date_of_birth="1990-01-01",
            mobile_phone1="0123456789",
        )
        response = self.client.get(CLIENTS_URL)
        clients = Client.objects.all().order_by("id")
        serializer = ClientSerializer(clients, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_client(self):
        # test creating a new client
        client = {
            "code": "CL003",
            "first_name": "client3",
            "last_name": "client3",
            "address": "Batna, Algeria",
            "date_of_birth": "1990-01-01",
            "mobile_phone1": "0123456789",
        }
        self.client.post(CLIENTS_URL, client)
        exists = Client.objects.filter(code=client["code"]).exists()
        self.assertTrue(exists)


class GetSingleClientTest(TestCase):
    """
     test module for GET single client API
    """

    def setUp(self):
        self.client = APIClient()

    def test_get_valid_single_client(self):
        client4 = Client.objects.create(
            code="CL004",
            first_name="client4",
            last_name="client4",
            address="Batna, Algeria",
            date_of_birth="1990-01-01",
            mobile_phone1="0123456789",
        )
        response = self.client.get(
            reverse(CLIENT_DETAIL, kwargs={"pk": client4.pk})
        )
        serializer = ClientSerializer(client4)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_client(self):
        response = self.client.get(
            reverse(CLIENT_DETAIL, kwargs={"pk": 6})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UpdateSingleClientTest(TestCase):
    """
    Test module for updating an existing client record
    """

    def setUp(self):
        self.client = APIClient()

    def test_valid_update_client(self):
        client5 = Client.objects.create(
            code="CL005",
            first_name="client5",
            last_name="client5",
            address="Batna, Algeria",
            date_of_birth="1990-01-01",
            mobile_phone1="0123456789",
        )
        updated_client5 = {
            "code": "CL005",
            "first_name": "client5",
            "last_name": "client5",
            "address": "11 Algiers, Algeria",
            "date_of_birth": "1990-01-01",
            "mobile_phone1": "0123456789"
        }
        response = self.client.put(
            reverse(CLIENT_DETAIL, kwargs={"pk": client5.pk}),
            data=json.dumps(updated_client5),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_client(self):
        client6 = Client.objects.create(
            code="CL006",
            first_name="client6",
            last_name="client6",
            address="Batna, Algeria",
            date_of_birth="1990-01-01",
            mobile_phone1="0123456789"
        )

        invalid_update_client6 = {
            "code": "CL006",
            "first_name": "client6",
            "last_name": "client6",
            "date_of_birth": "1990-01-01"
        }

        response = self.client.put(
            reverse(CLIENT_DETAIL, kwargs={"pk": client6.pk}),
            data=json.dumps(invalid_update_client6),
            content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleClientTest(TestCase):
    """
    Test module for deleting an existing client record
    """

    def setUp(self):
        self.client = APIClient()

    def test_valid_delete_client(self):
        client6 = Client.objects.create(
            code="CL006",
            first_name="client6",
            last_name="client6",
            address="Batna, Algeria",
            date_of_birth="1990-01-01",
            mobile_phone1="0123456789",
        )
        response = self.client.delete(
            reverse(CLIENT_DETAIL, kwargs={"pk": client6.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_client(self):
        response = self.client.delete(
            reverse(CLIENT_DETAIL, kwargs={"pk": 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


# orders
class OrderApiTest(TestCase):
    """
    test the Order
    """

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_orders_list(self):
        # Test retrieving a list of orders
        client = Client.objects.create(
            code="CL001",
            first_name="client1",
            last_name="client1",
            address="Batna, Algeria",
            date_of_birth="1990-01-01",
            mobile_phone1="0123456789",
        )
        product1 = Product.objects.create(
            code="PR001",
            name="Product 1",
            family="F001",
            price=200,
        )
        product2 = Product.objects.create(
            code="PR002",
            name="Product 2",
            family="F001",
            price=450,
        )
        order1 = Order.objects.create(
            code="O001",
            date="2021-01-12T22:39:37+01:00",
            client=client,
        )
        order2 = Order.objects.create(
            code="O002",
            date="2021-01-12T22:39:37+01:00",
            client=client,
        )
        order3 = Order.objects.create(
            code="O003",
            date="2021-01-12T22:39:37+01:00",
            client=client,
        )

        order1.products.set([product1, product2])
        order2.products.set([product1])
        order3.products.set([product2])
        response = self.client.get(ORDERS_URL)
        orders = Order.objects.all().order_by("id")
        serializer = OrderSerializer(orders, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_order(self):
        # test creating a new order
        product1 = Product.objects.create(
            code="PR001",
            name="Product 1",
            family="F001",
            price=200,
        )
        product2 = Product.objects.create(
            code="PR002",
            name="Product 2",
            family="F001",
            price=200,
        )
        client = Client.objects.create(
            code="CL001",
            first_name="client1",
            last_name="client1",
            address="Batna, Algeria",
            date_of_birth="1990-01-01",
            mobile_phone1="0123456789",
        )
        order = {
            "code": "O001",
            "date": "2021-01-12T22:39:37+01:00",
            "client": client.pk,
            "products": [
                product1.pk,
                product2.pk
            ]
        }

        self.client.post(ORDERS_URL, data=json.dumps(order), content_type="application/json")
        exists = Order.objects.filter(code=order["code"]).exists()
        self.assertTrue(exists)


class GetSingleOrder(TestCase):
    """
     test module for GET single order API
    """

    def setUp(self):
        self.client = APIClient()

    def test_get_valid_single_order(self):
        client = Client.objects.create(
            code="CL001",
            first_name="client1",
            last_name="client1",
            address="Batna, Algeria",
            date_of_birth="1990-01-01",
            mobile_phone1="0123456789",
        )
        product1 = Product.objects.create(
            code="PR001",
            name="Product 1",
            family="F001",
            price=200,
        )
        product2 = Product.objects.create(
            code="PR002",
            name="Product 2",
            family="F001",
            price=450,
        )
        order = Order.objects.create(
            code="O001",
            date="2021-01-12T22:39:37+01:00",
            client=client,
        )
        order.products.set([product1, product2])
        response = self.client.get(
            reverse(ORDER_DETAIL, kwargs={"pk": order.pk})
        )
        serializer = OrderSerializer(order)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_order(self):
        response = self.client.get(
            reverse(ORDER_DETAIL, kwargs={"pk": 2})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UpdateSingleOrderTest(TestCase):
    """
    Test module for updating an existing order record
    """

    def setUp(self):
        self.client = APIClient()
        self.client1 = Client.objects.create(
            code="CL001",
            first_name="client1",
            last_name="client1",
            address="Batna, Algeria",
            date_of_birth="1990-01-01",
            mobile_phone1="0123456789",
        )
        self.product1 = Product.objects.create(
            code="PR001",
            name="Product 1",
            family="F001",
            price=200,
        )
        self.product2 = Product.objects.create(
            code="PR002",
            name="Product 2",
            family="F001",
            price=450,
        )
        self.order = Order.objects.create(
            code="O001",
            date="2021-01-12T22:39:37+01:00",
            client=self.client1,
        )

    def test_valid_update_order(self):
        self.order.products.set([self.product1, self.product2])
        updated_order = {
            "code": self.order.code,
            "date": "2021-01-12T22:39:37+01:00",
            "client": self.client1.pk,
            "products": [
                self.product1.pk,
            ]
        }
        response = self.client.put(
            reverse(ORDER_DETAIL, kwargs={"pk": self.order.pk}),
            data=json.dumps(updated_order),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_order(self):
        invalid_update_order = {
            "code": self.order.code,
            "date": "2021-01-12T22:39:37+01:00",
            "client": 55,
            "products": [
                self.product1.pk,
                self.product2.pk
            ]
        }

        response = self.client.put(
            reverse(ORDER_DETAIL, kwargs={"pk": self.order.pk}),
            data=json.dumps(invalid_update_order),
            content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleOrderTest(TestCase):
    """
    Test module for deleting an existing order record
    """

    def setUp(self):
        self.client = APIClient()
        self.client1 = Client.objects.create(
            code="CL001",
            first_name="client1",
            last_name="client1",
            address="Batna, Algeria",
            date_of_birth="1990-01-01",
            mobile_phone1="0123456789",
        )
        self.product1 = Product.objects.create(
            code="PR001",
            name="Product 1",
            family="F001",
            price=200,
        )
        self.product2 = Product.objects.create(
            code="PR002",
            name="Product 2",
            family="F001",
            price=450,
        )
        self.order = Order.objects.create(
            code="O001",
            date="2021-01-12T22:39:37+01:00",
            client=self.client1,
        )
        self.order.products.set([self.product1, self.product2])

    def test_valid_delete_order(self):
        response = self.client.delete(
            reverse(ORDER_DETAIL, kwargs={"pk": self.order.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_order(self):
        response = self.client.delete(
            reverse(ORDER_DETAIL, kwargs={"pk": 2}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class GetTotalPriceTest(TestCase):
    """
    Test module for calculating the total price for an order
    """

    def setUp(self):
        self.client = APIClient()
        self.client1 = Client.objects.create(
            code="CL001",
            first_name="client1",
            last_name="client1",
            address="Batna, Algeria",
            date_of_birth="1990-01-01",
            mobile_phone1="0123456789",
        )
        self.product1 = Product.objects.create(
            code="PR001",
            name="Product 1",
            family="F001",
            price=200,
        )
        self.product2 = Product.objects.create(
            code="PR002",
            name="Product 2",
            family="F001",
            price=450,
        )
        self.order1 = Order.objects.create(
            code="O001",
            date="2021-01-12T22:39:37+01:00",
            client=self.client1,
        )
        self.order1.products.set([self.product1, self.product2])
        self.order2 = Order.objects.create(
            code="O002",
            date="2021-01-12T22:39:37+01:00",
            client=self.client1,
        )

    def test_total_price(self):
        self.assertEqual(self.order1.total_price(), 650.0)
        self.assertEqual(self.order2.total_price(), 0)


