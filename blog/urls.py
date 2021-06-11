from . import views
# from django.urls import include

from django.urls import path
from .feeds import LatestPostsFeed, AtomSiteNewsFeed
from django.conf import settings
from django.conf.urls.static import static
# from .views import PostNewView

urlpatterns = [
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("conact/", views.contact, name="contact"),
    path("new/", views.new, name="new"),

    # path("new/", PostNewView.as_view(), name="new"),
    path("feed/atom", AtomSiteNewsFeed()),
    path("", views.PostList.as_view(), name="home"),
    path("client_post/", views.ClientPostList.as_view(), name="client_post"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    # path("summernote/", include("django_summernote.urls")),


]



