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
        print('----NMMMM',request.body)
        
        url = 'https://ussouthcentral.services.azureml.net/workspaces/151730822d384e008f146bde06c76aaa/services/14fd15e525ba4c7bb74f0565d5d167c5/execute?api-version=2.0&details=true'
        headers = {'Content-Type': 'application/json','Authorization':'Bearer vEDXpoF6UlR2w7/kJpPDQkR4BUE+1sLPCUDpYPoE2epXJm+gb93XRsDwa/972qT4wrx04P617W33H21GivQFGQ=='}
        payload = {"Inputs": {
                    "input1": {
                        "ColumnNames": [
                            "Marital Status",
                            "Gender",
                            "Income",
                            "Children",
                            "Cars",
                            "Age",
                            "Education",
                            "Occupation",
                            "Home Owner",
                            "Commute Distance",
                            "Region"
                        ],
                        "Values": [
                            [
                                "Married",
                                "Male",
                                "10000",
                                "0",
                                "2",
                                "18",
                                "graduate",
                                "managment",
                                "yes",
                                "0-1 miles",
                                "Europe"
                            ]
                        ]
                    }
                },
                "GlobalParameters": {}
            }
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