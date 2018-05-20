from django.urls import path

from django.urls import path

from price_entry import views


urlpatterns = [
    path('', views.enter_price, name='enter_price'),
    path('good_submit', views.good_submit, name='good_submit'),
]
