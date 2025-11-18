from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Blog, BlogCategory
from .serializer import BlogCategorySerial, BlogSerial
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class BlogListAPI(ListAPIView):
    queryset = BlogCategory.objects.filter(status=1)
    serializer_class = BlogCategorySerial

class BlogCategoryAPI(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerial
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

# Create your views here.
def get_hello(request):
    return HttpResponse(200)