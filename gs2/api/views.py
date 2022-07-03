#from urllib import response
#from django.shortcuts import render
import json
from rest_framework.renderers import JSONRenderer
from  django.http import HttpResponse
from .serializers import StudentSerializer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        print(json_data)
        str = io.BytesIO(json_data)
        python_data = JSONParser().parse(str)
        s = StudentSerializer(data=python_data)
        if s.is_valid():
            s.save()
            res = {'msg': 'data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(s.errors)
        return HttpResponse(json_data, content_type = 'application/json')





