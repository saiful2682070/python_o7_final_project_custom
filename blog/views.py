from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin
from blog.models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def about(request):
    return render(request, 'blog/about.html', {"title": "About Page"})


def home(request):
    blog_post = Post.objects.all()
    return render(request, 'blog/home.html', {"blog_post": blog_post})


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'blog_post'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

