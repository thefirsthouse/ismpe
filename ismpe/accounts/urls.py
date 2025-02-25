from django.urls import path
# from .views import RegisterView
from django.contrib.auth.views import LogoutView as DjangoLogoutView, LoginView

urlpatterns = [
    # path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', DjangoLogoutView.as_view(), name='logout')
]
