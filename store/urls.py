from django.urls import path
from .views import StoreDetailView


urlpatterns = [
    path('store', StoreDetailView.as_view())
]