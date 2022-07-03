from django.shortcuts import render
from .models import Student
from .serializers import helloSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer

#Model Object - Single Student Data
def student_details(request, pk):
    stu = Student.objects.get(id =pk)                                                   #complex object
   # print(stu)
    s = helloSerializer(stu)                                                         #python object
    return JsonResponse(s.data)
   # print(s)
   # print(s.data)
 #   json_data = JSONRenderer().render(s.data)                                          # json data
  #  print(json_data)
  #  return HttpResponse(json_data, content_type='application/json')                    #respose json data to client

#Query set- all student data

def student_list(request):
    stu = Student.objects.all()                                                   #complex object
   # print(stu)
    s = helloSerializer(stu, many=True)                                                         #python object
   # print(s)
  #  print(s.data)
  #  json_data = JSONRenderer().render(s.data)                                          # json data
  #  print(json_data)
  #  return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(s.data, safe= False)