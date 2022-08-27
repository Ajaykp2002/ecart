
from django.urls import path
from . import views
from ecart import settings
app_name='ecartapp'
urlpatterns = [
    path('',views.allprocat,name='allprocat'),
    path('<slug:c_slug>/',views.allprocat,name="probycat"),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodet,name="prodet"),
]