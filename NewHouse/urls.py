from django.urls import path
from NewHouse import views
urlpatterns=[
    # path('login/',views.checkLogin),
    path('selectAll/',views.select_all),
    path('update/',views.save_or_update),
    path('delete/',views.delete),
    path('selectByPattern/',views.select_by_pattern),
]