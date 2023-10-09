from django.urls import path
from . import views

app_name = 'account'


urlpatterns = [
    path('login' , views.login_page , name="login_page"),
    path('logout' , views.log_out , name="log_out"),
    path('register' , views.register_page , name="register_page"),
    path('edit' , views.edit_page , name="edit Page"),
]
