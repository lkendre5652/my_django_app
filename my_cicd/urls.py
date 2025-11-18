from django.urls import path
from .views import *

urlpatterns = [
    path('', get_hello, name='hello'),
    path('cats-blog/', BlogListAPI.as_view(), name='BlogListAPI'),
    path('blog-cats/', BlogCategoryAPI.as_view(), name='BlogCategoryAPI'),
]