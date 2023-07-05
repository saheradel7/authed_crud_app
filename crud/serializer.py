from rest_framework.serializers import ModelSerializer
from crud.models import User,Product,Order

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'