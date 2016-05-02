from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from django.conf import settings
import pymysql
import json
import random





def home(request):

	template = 'demo/index.html'
	context = {}

	return render(request,template, context)

def random_item(request):

	item = get_random_item()
	print (item[0][0])

	response_dict = {
		'product_title': item[0][0],
		'product_description': item[0][1],
		'product_image': item[0][2],
		'product_category':item[0][3]
	}

	json_response = json.dumps(response_dict)

	return HttpResponse(json_response, content_type='application/json')






##Helpers##


def query(query_string, items=None, safe_mode=True):
    """ Given a query string returns a cursor object """
   
    connection = pymysql.connect(**settings.MYSQL_DATABASE)
    cursor = connection.cursor()
    cursor.execute(query_string, items)
    connection.commit()
    return cursor.fetchall()



def get_random_item():
    number = random.randint(1,30000)
    return query(
        '''
        SELECT product_name, product_description, product_picture, B.subCategory_name
        FROM tblProduct
        JOIN tblSubCategory B
        	ON B.subCategory_id = tblProduct.subCategory_id
        WHERE product_id = {}
        '''.format(number)
    )