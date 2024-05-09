
from django.urls import include, path
from .views import authView,home, info_form

urlpatterns= [
    path("", home, name="home"),
    path("signup/",authView, name="authView"),
    path('info/', info_form, name='info_form'),
    path("account/", include("django.contrib.auth.urls")),
]