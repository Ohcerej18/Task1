from .import views
from django.urls import path
from .views import UserLoginView, RegisterView
from django.contrib.auth.views import LogoutView
from .views import taskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView

urlpatterns = [
    # path("admin/", admin.site.urls),
    path ('', UserLoginView.as_view(), name="login"),
    path ('register/', views.RegisterView, name="register"),
    path ('logout/', LogoutView.as_view(next_page="login"), name='logout'),
    path ('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/', taskList.as_view(), name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(), name='task'),
    path('task-create/',TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>/',DeleteView.as_view(),name='task-delete'),

]
