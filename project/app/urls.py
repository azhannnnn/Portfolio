from django.urls import path
from .views import *

urlpatterns = [
   
    
    path('', index,name="about"),
    path('resume/', resume,name="resume"),
    path('blog/', blog,name="blog"),
    path('portfolio/', portfolio,name="portfolio"),
    path('contact/', contact,name="contact"),

    path('send/',send,name="send")
]
