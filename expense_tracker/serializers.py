from rest_framework import serializers 
from expense_tracker.models import UserDetail

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ('id', 'user',  'address', 'created_date', 'modified_date')
    