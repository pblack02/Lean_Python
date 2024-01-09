from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import generic
from groups.models import Group, GroupMember
from . import models
from django.core.paginator import Paginator


class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
    model = Group

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class SingleGroup(generic.DetailView):
    model = Group
    template_name = 'groups/group_detail.html'

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.order_by('-members')
    #     return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch the posts related to the group
        posts_list = self.object.posts.all()  # This uses the 'posts' related_name in the Group model

        # Paginate the posts
        paginator = Paginator(posts_list, 3)  # Showing 3 posts per page
        page = self.request.GET.get('page')
        posts = paginator.get_page(page)

        # Add the paginated posts to the context
        context['posts'] = posts
        return context


class ListGroups(generic.ListView):
    paginate_by = 3
    model = Group

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-members')
        return queryset


class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))
        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(self.request, 'Warning already a member!')
        else:
            messages.success(self.request, 'You are now a member!')

        return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        try:
            membership = models.GroupMember.objects.filter(user=self.request.user, group__slug=self.kwargs.get('slug'))
        except models.GroupMember.DoesNotExist:
            messages.warning(self.request, 'Sorry, you are not a member of this group!')
        else:
            membership.delete()
            messages.success(self.request, 'You have left the group!')
        return super().get(request, *args, **kwargs)


class DeleteGroup(LoginRequiredMixin, generic.DeleteView):
    model = models.Group
    success_url = reverse_lazy('groups:all')

    def get_queryset(self):
        return super().get_queryset().filter(creator=self.request.user)

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Group has been deleted!')
        return response
