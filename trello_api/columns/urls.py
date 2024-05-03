
# urls.py
from django.urls import path
from .views import CreateColumnAPIView, ColumnRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', CreateColumnAPIView.as_view(), name='column-list'),
    path('<int:pk>/', ColumnRetrieveUpdateDestroyAPIView.as_view(), name='column-detail'),
]
