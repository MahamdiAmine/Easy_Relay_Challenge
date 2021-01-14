from django.db import models


class Product(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50, blank=True, default='')
    price = models.FloatField()
    remark = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.code


class Client(models.Model):
    code = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    date_of_birth = models.DateField()
    mobile_phone1 = models.CharField(max_length=13)
    mobile_phone2 = models.CharField(max_length=13, blank=True, default='')
    email = models.EmailField(max_length=30, blank=True, default='')
    company = models.CharField(max_length=35, blank=True, default='')

    def __str__(self):
        return self.code


class Order(models.Model):
    code = models.CharField(max_length=10, unique=True)
    date = models.DateTimeField(format('%Y-%m-%d %H:%m'))
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    products = models.ManyToManyField(Product, related_name='products')

    def __str__(self):
        return self.code

    def total_price(self):
        return sum([p.price for p in self.products.all()])
