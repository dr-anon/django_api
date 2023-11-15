from django.shortcuts import render
from .models import Drink,Student
from django.http import JsonResponse
from .serializers import DrinkSerializer,StudentSerializer

# Create your views here.
def drinks_api_view(request):
    data = Drink.objects.all()
    serialized_data = DrinkSerializer(data , many = "True")
    student_data = Student.objects.all()
    serialized_student_data = StudentSerializer(student_data, many = True)
    # return JsonResponse({"drinks":serialized_data.data},safe=False)
    Serializer_list = [{"students":serialized_student_data.data}, {"drinks":serialized_data.data}]

    content = { 
        'data': Serializer_list,    
        }
    return JsonResponse(content,safe=False)
