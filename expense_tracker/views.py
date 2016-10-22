from django.http.response import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from expense_tracker.models import UserDetail, ExpenseDetail
from django.views.decorators.csrf import csrf_exempt
from expense_tracker.serializers import UserDetailSerializer,\
    ExpenseDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
#####API call URL::: http://127.0.0.1:8000/expensetracker/user/


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
@api_view(['GET', 'POST', ])
def user_list(request):
    if request.method == 'GET':
        user_obj = UserDetail.objects.all()
        user_serializer = UserDetailSerializer(user_obj, many=True)
        # return JSONResponse(serializer.data)
        return Response(user_serializer.data)
    
    elif request.method == 'POST':
        print " inside==============posttttttt"
        data = JSONParser().parse(request)
        print "posttttttt data==========", data
        serializer = UserDetailSerializer(data=data)
        if serializer.is_valid():
            
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
                return Response(
                    serializer.errors, status=500)
                 
        return JSONResponse(serializer.errors, status=400)
    
#@csrf_exempt
@api_view(['GET', 'POST', ])
def expense_details(request):
    dict = {}
    if request.method == 'GET':
        expense_obj = ExpenseDetail.objects.all()#.select_related('user_detail')
        expense_serializer = ExpenseDetailSerializer(dict, many=True)
        print type(expense_serializer.data)
        return JSONResponse(expense_serializer.data)
       # return Response(expense_serializer.data)
       
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ExpenseDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
                return Response(serializer.errors, status=500)
                 
        return JSONResponse(serializer.errors, status=400)
        


    












        
