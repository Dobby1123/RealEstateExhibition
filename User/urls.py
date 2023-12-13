from django.urls import path
from User import views
urlpatterns=[
    path('login/',views.checkLogin),
    # path('save/',views.save)
]