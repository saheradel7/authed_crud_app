from django.urls import path

from . import views , api

urlpatterns = [
    path("index/", views.index , name="index"),
    path("alluser/", api.UserDetail.as_view() , name="user"),
    path("userinfo/<int:id>", api.UserInfo.as_view() , name="user"),

]





"""     path('user/', api.user_list),
    path('user/<int:id>/', api.user_detail),
] """