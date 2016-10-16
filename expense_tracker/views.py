from django.http.response import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from expense_tracker.models import UserDetail
from django.views.decorators.csrf import csrf_exempt
from expense_tracker.serializers import UserDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
#####API call URL::: http://127.0.0.1:8000/expensetracker/user/

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    print "inside========jsonres============="
    
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        print "content==============", content
        print "kwargs======",kwargs
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
@api_view(['GET', 'POST', ])
def user_list(request):
    print "inside===user list=================="
    if request.method == 'GET':
        user_obj = UserDetail.objects.all()
        print" user_obj=============", user_obj
        user_serializer = UserDetailSerializer(user_obj, many=True)
        return Response(user_serializer.data)
        
        
