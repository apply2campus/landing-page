
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('Register',views.forms, name='form'),
    path('why-learning-a-foreign-language-is-crucial-for-studying-abroad',views.blog1, name='blog1'),
    path('choosing-the-perfect-study-abroad-program-a-step-by-step-guide',views.blog2, name='blog2'),
    path('top-scholarship-opportunities-for-international-students-in-2023-a-comprehensive-guide',views.blog3, name='blog3'),
]
