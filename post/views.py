# -*- coding: utf-8 -*-



from .models import Post
from comment.models import Comment
from like.models import Like
from django.views.generic import CreateView, UpdateView, View
from django.shortcuts import resolve_url, get_object_or_404, HttpResponse

#class Post_Update(UpdateView):

  # template_name = 'post/edit_post.html'
  # model = Post
   #fields = 'title', 'text'

  # def get_queryset(self):
     # return super(Post_Update, self).get_queryset().filter(author = self.request.user)
  # def get_success_url(self):
     # return reverse('posts:currentpost',kwargs={'pk': self.object.pk})


class EditPost(UpdateView):

    template_name = 'post/edit_post.html'
    model = Post
    fields = 'title','text'

    def get_queryset(self):
        return super(EditPost, self).get_queryset().filter(author=self.request.user)

    def form_valid(self, form):
        super(EditPost,self).form_valid(form)
        return HttpResponse("OK")

    def get_success_url(self):
        #return self.request.META['HTTP_REFERER']
        return resolve_url('blogs:currentblog', pk=self.object.pk)


class Post_page(CreateView):

    template_name = "post/post_page.html"
    model = Comment
    fields = ('text',)


    def get_context_data(self, **kwargs):
        context = super(Post_page, self).get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.kwargs.get('pk'))
        return context

    def get_success_url(self):
       return resolve_url('posts:currentpost', pk=self.object.post.pk)


    def form_valid(self, form):
       form.instance.author = self.request.user
       form.instance.post_id = self.kwargs.get('pk')
       return super(Post_page, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return super(Post_page, self).post(self, request, *args, **kwargs)
        else:
            return resolve_url('login')

class Post_comments(CreateView):

        template_name = "post/commentsdiv.html"
        model = Comment
        fields = ('text',)

        def get_context_data(self, **kwargs):
            context = super(Post_comments, self).get_context_data(**kwargs)
            context['post'] = Post.objects.get(pk=self.kwargs.get('pk'))
            return context

        def get_success_url(self):
            return resolve_url('posts:postcomments', pk=self.object.post.pk)

        def form_valid(self, form):
            form.instance.author = self.request.user
            form.instance.post_id = self.kwargs.get('pk')
            return super(Post_page, self).form_valid(form)

        def post(self, request, *args, **kwargs):
            if request.user.is_authenticated():
                return super(Post_page, self).post(self, request, *args, **kwargs)
            else:
                return resolve_url('login')

class PostLikeView(View):

        post_object = None

        def dispatch(self, request, pk=None, *args, **kwargs):
            self.post_object = get_object_or_404(Post, id=pk)
            return super(PostLikeView, self).dispatch(request, *args, **kwargs)

        def post(self, *args, **kwargs):
            like = self.post_object.likes.filter(author=self.request.user).first()
            if like is None:
                like = Like()
                like.author = self.request.user
                like.post = self.post_object
                like.save()
            else:
                like.delete()

            return HttpResponse(Like.objects.filter(post=self.post_object).count())

# Create your views here.
