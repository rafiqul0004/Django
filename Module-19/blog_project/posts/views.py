from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .import forms
from .import models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
# Create your views here.
# @login_required 
# def add_posts(request):
#     if request.method == 'POST':
#         post_form=forms.PostForm(request.POST)
#         if post_form.is_valid():
#             post_form.instance.author=request.user
#             post_form.save()
#             return redirect('add_posts')
#     else:
#         post_form=forms.PostForm()
#     return render(request,'add_post.html',{'form':post_form})

@method_decorator(login_required,name='dispatch')
class AddPostView(CreateView):
     model=models.Post
     form_class=forms.PostForm
     template_name='add_post.html'
     success_url=reverse_lazy('add_posts')
     def form_valid(self, form):
          form.instance.author=self.request.user
          return super().form_valid(form)


# @login_required 
# def edit_posts(request,id):
#     post=models.Post.objects.get(pk=id)
#     post_form=forms.PostForm(instance=post)
#     if request.method == 'POST':
#         post_form=forms.PostForm(request.POST,instance=post)
#         if post_form.is_valid():
#             post_form.instance.author=request.user
#             post_form.save()
#             return redirect('homepage')
#     return render(request,'add_post.html',{'form':post_form})

@method_decorator(login_required,name='dispatch')
class EditPostView(UpdateView):
      model=models.Post
      form_class=forms.PostForm
      template_name='add_post.html'
      pk_url_kwarg = 'id'
      success_url=reverse_lazy('profile')


# @login_required 
# def delete_posts(request,id):
#         post=models.Post.objects.get(pk=id)
#         post.delete()
#         return redirect('homepage')

@method_decorator(login_required,name='dispatch')
class DeletePostView(DeleteView):
     model=models.Post
     template_name='delete.html'
     pk_url_kwarg = 'id'
     success_url=reverse_lazy('profile')

class DetailPostView(DetailView):
     model=models.Post
     template_name='detail_post.html'
     pk_url_kwarg='id'

     def post(self, request, *args, **kwargs):
          comment_form=forms.CommentForm(self.request.POST)
          post=self.get_object()
          if comment_form.is_valid():
               new_comment=comment_form.save(commit=False)
               new_comment.post=post
               new_comment.save()
          return self.get(request, *args, **kwargs)

     def get_context_data(self,**kwargs):
          context=super().get_context_data(**kwargs)
          post=self.object
          comments=post.comments.all()

          comment_form=forms.CommentForm()
          context['comments']=comments
          context['comment_form']=comment_form
          return context

          