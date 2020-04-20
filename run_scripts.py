#!/usr/bin/env python3

# initialize django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'ArcticApi.settings'
import django
django.setup()

# regular imports
from api.models import Category, Product, AppStore
import json
import csv
import pandas as pd
# main script
def main():
    db = AppStore()
    for a in AppStore.objects.all():
        a.delete()

    
    data = pd.read_csv('FinalProjectDataset.csv')
    print(data)
    cnt = 0
    
    for item in data.values:
        db.id = item[0]
        db.track_name = item[1]
        db.size_bytes = item[2]
        db.currency = item[3]
        db.price = item[4]
        db.rating_count_tot = item[5]
        db.rating_count_ver = item[6]
        db.user_rating  = item[7]
        db.user_rating_ver = item[8]
        db.ver = item[9]
        db.cont_rating = item[10]
        db.prime_genre = item[11]
        db.sup_devices_num = item[12]
        db.ipadsc_urls_num = item[13]
        db.lang_num = item[14]
        db.vpp_lic = item[15]
        db.app_desc = item[16]
        db.save()
        cnt +=1
        print(cnt)
        
            
    # cat_list = [] #this will hold the categoreis
    # with open('products.json') as json_file:
    #     data = json.load(json_file)
    # products = data['PRODUCTS']
    # print(products, '<----')
    # for prod in products:
    #     dbprod = Product()
    #     dbprod.id = prod['id']
    #     if prod['category'] not in cat_list: #this sees if we already have a categore ie dont make more categories than we need
    #         cat_list.append(prod['category'])
    #         Category.objects.create(title=prod['category'])
    #     dbprod.category = Category.objects.filter(title=prod['category']).first()
    #     print('-------------------------------------------------------------------',Category.objects.filter(title=prod['category']).first())
    #     # print(Category.objects.filter(title=prod['category']).first())
    #     dbprod.filename = prod['filename']
    #     dbprod.name = prod['name']
    #     dbprod.description = prod['description']
    #     dbprod.price = prod['price']
    #     dbprod.save()
    


# bootstrap
if __name__ == '__main__':
    main()
