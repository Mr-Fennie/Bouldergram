from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView, CreateView,
                                    UpdateView, DeleteView, TemplateView)
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, AddCommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.

class Home(ListView):
    model = Post
    template_name = 'home.html'
    #rearrange post list
    #ordering = ['-id']
    ordering = ['-post_date','-post_time']

class AboutView(TemplateView):
    template_name = 'about.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


    #context for like/dislike button
    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)

        like = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = like.total_likes()
        liked = False
        if like.likes.filter(id=self.request.user.id).exists():
            liked = True


        dislike = get_object_or_404(Post, id=self.kwargs['pk'])
        total_dislikes = dislike.total_dislikes()
        disliked = False

        if dislike.dislikes.filter(id=self.request.user.id).exists():
            disliked = True


        context['total_likes'] = total_likes
        context['liked'] = liked
        context['total_dislikes'] = total_dislikes
        context['disliked'] = disliked
        return context



class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #Anternative selective fields
    #fields = ('title', 'author', 'body')

class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'add_comment.html'
    ordering = ['-date_added']

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.name = self.request.user.username

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})


class AddCountryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_country.html'
    fields = '__all__'
    #Anternative selective fields
    #fields = ('title', 'author', 'body')


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')



#########################################################

def CountryView(request, cont):
    country_posts = Post.objects.filter(country__iexact=cont.replace('-',' ')).order_by('-post_date','-post_time')
    return render(request, 'countries.html', {'cont':cont.title().replace('-',' '), 'country_posts':country_posts})

def CountryListView(request):
    country_menu_list = Category.objects.all().order_by('country')
    return render(request, 'country_list.html', {'country_menu_list':country_menu_list})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

def DislikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('dislike_post_id'))
    disliked = False
    if post.dislikes.filter(id=request.user.id).exists():
        post.dislikes.remove(request.user)
    else:
        post.dislikes.add(request.user)
        disliked = True

    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))
