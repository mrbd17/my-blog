from django.urls import path
from . import views
urlpatterns = [
     path("", views.home, name="home"),
     path("login/",views.login_view,name='login'),
     path("logout/",views.logout_view, name = "logout"),
     path("register/",views.register,name = 'register'),
     path("/post/<int:post_id>/", views.post_detail,name='postdetial' ),
     path("post_create/", views.create_post,name = "postcreate"),
     path("update-post<int:post_id>/",views.update_post,name="update-post"),
     path("delete-post<int:post_id>/",views.delete_post,name="delete-post"),
     path('post/<int:post_id>/comment/', views.comment_view,name='add-comment'),
     
]
