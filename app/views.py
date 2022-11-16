from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from app.models import Post


# Create your views here.
class HomeView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'app/index.html'


class PostMylistView(ListView):
    model = Post
    template_name = 'app/post_mylist.html'

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)

class PostCreateView(CreateView):
    model = Post
    template_name = 'app/post_create.html'
    fields = ['content']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post
    template_name = 'app/post_detail.html'

class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'app/post_delete.html'
    model = Post
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied
        return obj

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['content']
    template_name = 'app/post_update.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied
        return obj

    success_url = reverse_lazy('index')
