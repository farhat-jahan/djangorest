from rest_framework.views import APIView
from models import Stock
from stockapi.serializers import StockSerializer
from django.http.response import HttpResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
import sys

# i will do this https://www.youtube.com/watch?v=c3yB0_4Yd48


class StockList(APIView):
    '''
    return all stock data or create stock data
    '''
    def get(self, request):
        ''' we will return all stock in a response '''
        stockobj = Stock.objects.all()
        serializerobj = StockSerializer(stockobj, many=True)
        return Response(serializerobj.data)
    
    def post(self, request):
        ''' we will create a new entry of stock '''
        data = JSONParser().parse(request)
        serializerobj = StockSerializer(data=data)
        if serializerobj.is_valid():
            serializerobj.save()
            #print serializerobj.data
            #{'modified_date': u'2016-11-20T19:36:08.952224Z', 'open': 24.9, 'volume': 600, 'created_date': u'2016-11-20T19:36:08.952136Z', 'close': 34.0, 'ticker': u'FB3', u'id': 5}
            return Response(serializerobj.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializerobj.errors, status = status.HTTP_400_BAD_REQUEST)
