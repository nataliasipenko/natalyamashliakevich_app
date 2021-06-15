from . import views
# from django.urls import include

from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
# from .views import PostNewView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


class MyHack(auth_views.PasswordResetView):
    success_url = reverse_lazy('password_reset_done')


urlpatterns = [

    path('all_topics', views.all_topics, name='all_topics'),
    path('topic/<slug:slug>/', views.topics_details, name='detail_topic'),

    path("conact/", views.contact, name="contact"),
    path("new/", views.new, name="new"),

    # path("new/", PostNewView.as_view(), name="new"),

    path("", views.PostList.as_view(), name="home"),

    path("<slug:slug>/login/", auth_views.LoginView.as_view()),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path('password_reset/', MyHack.as_view(), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy("password_reset_complete"),
    ), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    path('profile/', views.view_profile, name='profile'),
    path('register/', views.register, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

    path("client_post/", views.ClientPostList.as_view(), name="client_post"),
    path("post-detial/<str:slug>/", views.post_detail, name="post_detail"),
    path('post-detail/<str:slug>/share/', views.share_post,
         name='share_post'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
