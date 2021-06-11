from . import views
# from django.urls import include

from django.urls import path
from .feeds import LatestPostsFeed, AtomSiteNewsFeed
from django.conf import settings
from django.conf.urls.static import static
# from .views import PostNewView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("conact/", views.contact, name="contact"),
    path("new/", views.new, name="new"),

    # path("new/", PostNewView.as_view(), name="new"),
    path("feed/atom", AtomSiteNewsFeed()),
    path("", views.PostList.as_view(), name="home"),
    path("<slug:slug>/login/", auth_views.LoginView.as_view()),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("client_post/", views.ClientPostList.as_view(), name="client_post"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),

    # path("summernote/", include("django_summernote.urls")),



]



