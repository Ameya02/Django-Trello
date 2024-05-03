# urls.py
from django.urls import path
from .views import AddCardAPIView, EditCardAPIView, ReorderCardAPIView

urlpatterns = [
    path('', AddCardAPIView.as_view(), name='add-card'),
    path('<int:pk>/', EditCardAPIView.as_view(), name='edit-card'),
    path('reorder/', ReorderCardAPIView.as_view(), name='reorder-card'),

]
