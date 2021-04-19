from django.urls import path
from basic_app import views

# SET THE NAMESPACE! FOR TEMPLATE TAGGING! = name followed by name of app
app_name = 'basic_app'

urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
