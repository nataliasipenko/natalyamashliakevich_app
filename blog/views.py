from django.views import generic
# from django_summernote.widgets import SummernoteInplaceWidget

from .forms import CommentForm
from .forms import ClientPostForm
from django.shortcuts import render, get_object_or_404, redirect
from . import models
from django.contrib.auth.decorators import login_required

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


@login_required()
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
