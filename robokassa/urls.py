from django.conf.urls import url

from . import views

app_name = "robokassa"

urlpatterns = [
    url(r"^result/$", views.receive_result, name="result"),
    url(r"^success/$", views.success, name="success"),
    url(r"^fail/$", views.fail, name="fail"),
]
