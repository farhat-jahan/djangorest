from rest_framework import serializers
from models import Stock

class StockSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Stock
        #fields = ('ticker', 'volume')#if u want to return only these two fields then uncomment this
        #fields = '__all__' # if u wnat to send all details even id also(if not dont define it))
        # if u will not define any above, default it will return all data including id