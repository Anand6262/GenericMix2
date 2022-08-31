from . models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListCreateAPIView #Type of Concrete View Classes
from rest_framework.generics import RetrieveUpdateDestroyAPIView #Type of Concrete View Classes

# # Create your views here


#To GET all data(List)   and   To POST data(Create)
class StudentListCreate(ListCreateAPIView): #pk(primary key is not required)
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

#To GET specific data(Retrieve)   and   To PUT/PATCH data(Update)   and   To DELETE data(Destroy)
class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView): #pk(Primary key is required)
    queryset=Student.objects.all()
    serializer_class=StudentSerializer






# #GenericAPIView and Model Mixin
# from . models import Student
# from .serializers import StudentSerializer
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin
# from rest_framework.mixins import RetrieveModelMixin
# from rest_framework.mixins import CreateModelMixin
# from rest_framework.mixins import UpdateModelMixin
# from rest_framework.mixins import DestroyModelMixin

# # Create your views here

# #To GET data and POST data
# class StudentListCreateAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

#     #To GET data
#     def get(self, request, *args, **kwargs): # for ListModelMixin
#         print('\n<<<<<<<<<<<<<<<<GET>>>>>>>>>>>>>>')
#         return self.list(request, *args, **kwargs)

#     #To POST data
#     def post(self, request, *args, **kwargs): # For CreateModelMixin
#         print('\n<<<<<<<<<<<<<<<<POST>>>>>>>>>>>>>>')
#         return self.create(request, *args, **kwargs)


# #To GET(specific data), PUT data, DELETE data
# class StudentRetrieveUpdateDestroyAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

#     #To GET specific data
#     def get(self, request, *args, **kwargs):
#         print('\n<<<<<<<<<<<<<<<<GET(Specific)>>>>>>>>>>>>>>')
#         return self.retrieve(request, *args, **kwargs)

#     #To PUT data
#     def put(self, request, *args, **kwargs):
#         print('\n<<<<<<<<<<<<<<<<PUT>>>>>>>>>>>>>>')
#         return self.update(request, *args, **kwargs)

#     #To PATCH data
#     def patch(self, request, *args, **kwargs):
#         print('\n<<<<<<<<<<<<<<<<PATCH>>>>>>>>>>>>>>')
#         return self.partial_update(request, *args, **kwargs)

#     #To DELETE data
#     def delete(self, request, *args, **kwargs):
#         print('\n<<<<<<<<<<<<<<<<DELETE>>>>>>>>>>>>>>')
#         return self.destroy(request, *args, **kwargs)