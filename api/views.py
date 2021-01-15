from rest_framework import mixins, generics

from core.models import Product, Client, Order
from core.serializers import ProductSerializer, ClientSerializer, OrderSerializer


class CustomDetail(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin):
    lookup_field = 'pk'

    def get(self, request, pk=None):
        return self.retrieve(request)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


class CustomVIEW(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class ProductAPIView(CustomVIEW):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetails(CustomDetail):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ClientAPIView(CustomVIEW):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientDetails(CustomDetail):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class OrderAPIView(CustomVIEW):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderDetails(CustomDetail):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
