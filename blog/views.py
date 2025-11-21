from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

# Create your views here.


def blog_list(request):
    posts = Post.objects.all().order_by('-created')
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_details(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/blog_details.html', {'post': post})


def create_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        Post.objects.create(title=title, content=content)

        return redirect('blog_list')

    return render(request, 'blog/create_post.html')


# UPDATE (EDIT)
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('blog_details', id=post.id)

    return render(request, 'blog/edit_post.html', {'post': post})


# DELETE
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('blog_list')