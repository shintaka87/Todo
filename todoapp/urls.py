from django.contrib import admin
from django.urls import path
from .views import TodoList, TodoCreate, TodoUpdate, TodoDelete

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', TodoList.as_view(), name='list'),
  path('create/', TodoCreate.as_view(), name='create'),
  path('update/<int:pk>/', TodoUpdate.as_view(), name='update'),
  path('delete/<int:pk>/', TodoDelete.as_view(), name="delete"),
]