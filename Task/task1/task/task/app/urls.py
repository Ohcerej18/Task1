from .import views
from django.urls import path
from .views import UserLoginView, RegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path("admin/", admin.site.urls),
    path ('', UserLoginView.as_view(), name="login"),
    path ('register/', views.RegisterView, name="register"),
    path ('logout/', LogoutView.as_view(next_page="login"), name='logout'),
    path ('dashboard/', views.dashboard, name="dashboard"),

]
