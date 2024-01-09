from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic
from braces.views import SelectRelatedMixin
from . import models
from . import forms
from django.contrib.auth import get_user_model
from groups.models import Group

User = get_user_model()


# Create your views here

class PostList(SelectRelatedMixin, generic.ListView):
    paginate_by = 3
    model = models.Post
    select_related = ('user', 'group')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            # Adjusting how to retrieve the user's groups based on your GroupMember model
            user_groups = models.Group.objects.filter(memberships__user=self.request.user)
            context['get_user_groups'] = user_groups
        return context


class UserPost(generic.ListView):
    paginate_by = 3
    model = models.Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context


class PostDetail(SelectRelatedMixin, generic.DetailView):
    paginate_by = 3
    model = models.Post
    select_related = ('user', 'group')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user__username__iexact=self.kwargs.get('username'))
        queryset = queryset.order_by('-created_at')
        return queryset


class CreatePost(LoginRequiredMixin, generic.CreateView, SelectRelatedMixin):
    fields = ('message', 'group')
    model = models.Post

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, generic.DeleteView, SelectRelatedMixin):
    model = models.Post
    select_related = ('user', 'group')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Post Deleted')
        return super().delete(*args, **kwargs)
