from django.views import generic
# from django_summernote.widgets import SummernoteInplaceWidget

from .forms import CommentForm
from .forms import ClientPostForm
from django.shortcuts import render, get_object_or_404, redirect
from . import models
from django.contrib.auth.decorators import login_required

from . import forms
from django.http import HttpResponse
from django.contrib.auth.models import User


# from django.views.generic import CreateView


# Create your views here.
# from .models import ClientPost


class ClientPostList(generic.ListView):
    queryset = models.ClientPost.objects.filter(active=True).order_by("-created_on")
    template_name = "client_posts.html"


class PostList(generic.ListView):
    queryset = models.Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3


@login_required
def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(models.Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )


def new(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        file = request.POST['file']
        author = request.POST['author']
        newpost = models.ClientPost(title=title, content=content, file=file, author=author)
        newpost.save()
        return redirect("/")
    context = {}
    return render(request,
                  'post_edit.html',
                  context)


def contact(request):
    if request.method == "POST":
        email = request.POST['email']
        message = request.POST['message']
        newmage = models.Contactmessage(email=email, message=message)
        newmage.save()
        return redirect("/")
    context = {}
    return render(request,
                  'contacts.html',
                  context)


# class PostNewView(CreateView):
#     model = ClientPost
#     form_class = ClientPostForm
#     template_name = "post_edit.html"
#     fields = ['title', 'content', 'file']
#
# def get_form(self, form_class):
#     form = super(PostNewView, self).get_form(form_class)
#     form.fields['content'].widget = SummernoteInplaceWidget()
#     return form

def view_profile(request):
    return render(request,
                  'profile.html')


def register(request):
    if request.method == "POST":
        user_form = forms.RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            models.Profile.objects.create(user=new_user, photo='unknown.jpg')
            return render(request, 'registration/reg_complete.html',
                          {'new_user': new_user})
        else:
            return HttpResponse('bad credentials')
    else:
        user_form = forms.RegistrationForm()
        return render(request, 'registration/register_user.html',
                      {'form': user_form})


@login_required
def edit_profile(request):
    if request.method == "POST":

        user_form = forms.UserEditForm(request.POST,
                                       instance=request.user)
        profile_form = forms.ProfileEditForm(request.POST,
                                             instance=request.user.profile,
                                             files=request.FILES)

        if profile_form.is_valid():
            if user_form.is_valid():

                if not profile_form.cleaned_data['photo']:
                    profile_form.cleaned_data['photo'] = request.user.profile.photo
                profile_form.save()
                user_form.save()
                return render(request, 'profile.html')

    else:
        user_form = forms.UserEditForm(request.POST,
                                       instance=request.user)
        profile_form = forms.ProfileEditForm(request.POST,
                                             instance=request.user.profile)
        return render(request,
                      'edit_profile.html',
                      {'user_form': user_form, 'profile_form': profile_form})


def all_topics(request):
    topic_list = models.Topic.objects.all()
    return render(request,
                  'all_topics.html',
                  {'topics': topic_list})


@login_required
def topics_details(request, slug):
    topic = get_object_or_404(models.Topic,
                              slug=slug)
    return render(request,
                  'detail_topic.html',
                  {'topic': topic})
