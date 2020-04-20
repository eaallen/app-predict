from rest_framework import routers, serializers, viewsets
from api.models import Category, Product, AppStore


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']   
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ['id', 'category', 'filename', 'name', 'description', 'price']
class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id',
                  'name',
                  'address1',
                  'address2',
                  'city',
                  'state',
                  'zipcode',
                  'total',
                  'items',
                  'payment_intent'
                ]   
class AppStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppStore
        fields = [
            'id',
            'track_name',
            'size_bytes',
            'currency',
            'price',
            'rating_count_tot',
            'rating_count_ver',
            'user_rating',
            'user_rating_ver',
            'ver',
            'cont_rating',
            'prime_genre',
            'sup_devices_num',
            'ipadSc_urls_num',
            'lang_num',
            'vpp_lic',
            'app_desc'
            ]   

        