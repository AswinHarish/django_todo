from django.urls import path
from .views import TaskList, TaskCreate, TaskUpdate, Delete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('create/', TaskCreate.as_view(), name='create'),
    path('task/<int:pk>/', TaskUpdate.as_view(), name='task'),
    path('delete/<int:pk>/', Delete.as_view(), name='delete'),
]
