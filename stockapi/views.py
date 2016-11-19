from rest_framework.views import APIView
from models import Stock
from stockapi.serializers import StockSerializer
from django.http.response import HttpResponse
from rest_framework.response import Response

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
        pass
