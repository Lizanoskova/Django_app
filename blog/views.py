# -*- coding: utf-8 -*-


from .models import Blog
from django.views.generic import ListView,CreateView
from post.models import Post
from django.shortcuts import render,get_object_or_404,resolve_url

class Blog_list(ListView):

    model = Blog
    context_object_name = 'blogs'
    template_name = "blog/blog_list.html"
    paginate_by = 5

class Blog_page(CreateView):

    model = Post
    template_name = "blog/blog_page.html"
    fields = 'title', 'text'


    def get_context_data(self, **kwargs):
        context = super(Blog_page, self).get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(pk=self.kwargs.get('pk'))
        return context

    def get_success_url(self):
       return resolve_url('blogs:currentblog', pk=self.object.blog.pk)


    def form_valid(self, form):
       form.instance.author = self.request.user
       form.instance.blog_id = self.kwargs.get('pk')
       return super(Blog_page, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return super(Blog_page, self).post(self, request, *args, **kwargs)
        else:
            return resolve_url('login')



#class Post_Create(CreateView):

   #template_name = 'blog/new_post.html'
   #model = Post
   #fields = 'title', 'text'

   #def get_context_data(self, **kwargs):
       #context = super(Post_Create, self).get_context_data(**kwargs)
       #context['post'] = Post.objects.get(pk=self.kwargs.get('pk'))
       #return context
    #def form_valid(self, form):
       #form.instance.author = self.request.user
       #form.instance.blog_id = self.kwargs.get('pk')
      # return super(Blog_page, self).form_valid(form)


   #def get_success_url(self):
      #return reverse('posts:currentpost',kwargs={'pk': self.object.pk})




