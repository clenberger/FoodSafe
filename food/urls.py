from django.urls import path

from . import views

urlpatterns = [
    path('', views.FoodListView.as_view(), name='index'),
    path('add_item/', views.FoodCreateView.as_view(), name="new_item_page"),
    path('delete/<item_id>',views.delete_item ,name='delete'),
]