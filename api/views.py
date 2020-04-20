from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Category
from api.models import Product
from api.models import Sale
from api.models import AppStore
from api.serializer import CategorySerializer, ProductSerializer, SaleSerializer,AppStoreSerializer
import json
import stripe
import requests


class AzureML(APIView):
    @csrf_exempt
    def post(self, request, format=None):
        print('----NMMMM',request.data)
        data=request.data
        # print('+++++++++++++++++++', request.body[0])
        url = 'https://ussouthcentral.services.azureml.net/workspaces/8a1c3ee5c1c34dd6bf7f601ac1718b3d/services/1fedfe88788b419f8ec10f5e4ee93615/execute?api-version=2.0&details=true'
        headers = {'Content-Type': 'application/json','Authorization':'Bearer 2xSFT5p90PXdI/A8JTavS49ieDBB4bWPaY6D9vGWs3W7YkoG7/QCQDwAZlN2ziEcY00mV0Mcx3/354Juh1QbVQ=='}
        payload = {"Inputs": {
                    "input1": {
                    "ColumnNames": [
                        "id",
                        "track_name",
                        "size_bytes",
                        "currency",
                        "price",
                        "rating_count_tot",
                        "rating_count_ver",
                        "user_rating",
                        "user_rating_ver",
                        "ver",
                        "cont_rating",
                        "prime_genre",
                        "sup_devices_num",
                        "ipadSc_urls_num",
                        "lang_num",
                        "vpp_lic",
                        "app_desc"
                    ],
                    "Values": [
                        [
                        '23453',
                        data[0],
                        data[1],
                        "USD",
                        data[2],
                        '2974676',
                        '212',
                        '3.5',
                        '3.5',
                        '95',
                        data[6],
                        data[7],
                        data[4],
                        '1',
                        data[5],
                        data[8],
                        data[3]
                        ]
                    ]
                    }
                },
                "GlobalParameters": {}
            }
        print('00000____>', payload)
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        print('from the azure studio--------->',r.json())
        return Response(r.text)
class AppStoreDetail(APIView):
    '''Work with an individual Category object'''
    @csrf_exempt
    def get(self, request, pk, format=None):
        cat = AppStore.objects.get(id=pk)
        serializer = AppStoreSerializer(cat)
        return Response(serializer.data)
    @csrf_exempt
    def post(self, request, pk, format=None):
        body = request.data
        print('this is the body',body)
        serializer = AppStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppStoreList(APIView):
    '''Get all apps or create an app'''
    @csrf_exempt
    def get(self, request, format=None):
        app = AppStore.objects.all()
        if request.query_params.get('title'):
            app = app.filter(title__contains=request.query_params.get('title'))
        serializer = AppStoreSerializer(app, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = AppStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryList(APIView):
    '''Get all categories or create a category'''
    @csrf_exempt
    def get(self, request, format=None):
        cats = Category.objects.all()
        if request.query_params.get('title'):
            cats = cats.filter(title__contains=request.query_params.get('title'))
        serializer = CategorySerializer(cats, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    '''Work with an individual Category object'''
    @csrf_exempt
    def get(self, request, pk, format=None):
        cat = Category.objects.get(id=pk)
        serializer = CategorySerializer(cat)
        return Response(serializer.data)

    @csrf_exempt
    def put(self, request, pk, format=None):
        cat = Category.objects.get(id=pk)
        serializer = CategorySerializer(cat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def delete(self, request, pk, format=None):
        cat = Category.objects.get(id=pk)
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class ProductList(APIView):
    '''Get all categories or create a category'''
    @csrf_exempt
    def get(self, request, format=None):
        cats = Product.objects.all()
        if request.query_params.get('title'):
            cats = cats.filter(title__contains=request.query_params.get('title'))
        serializer = ProductSerializer(cats, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    '''Work with an individual Category object'''
    @csrf_exempt
    def get(self, request, pk, format=None):
        cat = Product.objects.get(id=pk)
        serializer = ProductSerializer(cat)
        return Response(serializer.data)

    @csrf_exempt
    def put(self, request, pk, format=None):
        cat = Product.objects.get(id=pk)
        serializer = ProductSerializer(cat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def delete(self, request, pk, format=None):
        cat = Product.objects.get(id=pk)
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CreatSale(APIView):
    @csrf_exempt
    def post(self, request, format=None):
        body = json.loads(request.body)
        print('this is the body',body)
        sale = Sale()
        # sale.id = body['id']
        sale.name = body['name']
        sale.address1 = body['address1']
        sale.address2 = body['address2']
        sale.city = body['city']
        sale.state = body['state']
        sale.zipcode = body['zipcode']
        sale.total = body['total']
        sale.items = body['items']
        sale.payment_intent = stripe.PaymentIntent.create(
            amount = int(sale.total * 100),
            currency = 'usd',
        )
    
        sale.save()
        return Response({
            'sale_id': sale.id,
            'client_secret': sale.payment_intent['client_secret']
        })