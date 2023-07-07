from . import views , api
from django.urls import path

urlpatterns = [
    path("listuser/", api.UserDetail.as_view() , name="user"),
    path("changeuser/<int:id>", api.UserInfo.as_view() , name="user"),
    
]
