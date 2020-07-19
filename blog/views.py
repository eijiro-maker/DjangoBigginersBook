from django.shortcuts import redirect ,get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import CommentCreateForm
from .models import Post, Comment
# Create your views here.

class PostList(generic.ListView):
    model = Post
    ordering = '-created_at'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list']=Category.objects.all()
        context['tag_list'] = Tag.objects.all()
        return context


class PostDetail(generic.DetailView):
    model = Post

class CommentCreate(generic.CreateView):
    model = Comment
    form_class = CommentCreateForm

    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        return redirect('blog:post_detail', pk=post_pk)
