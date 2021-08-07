from django.urls import path
from first_app import views

app_name = 'first_app'
urlpatterns = [
    path('index', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('form', views.form_page, name='form_page'),
    path('relative', views.relative_page, name='relative_page'),
    path('other', views.other_page, name='other_page'),
    path('home', views.home, name='home'),
    path('registration', views.registration, name='registration'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
]
