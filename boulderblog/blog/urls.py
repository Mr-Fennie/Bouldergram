from django.urls import path
#from . import views
from .views import (Home, PostDetailView, AddPostView, UpdatePostView,
                    DeletePostView, AddCountryView, CountryView,
                    CountryListView, LikeView, DislikeView, AddCommentView,
                    AboutView )


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about' ),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('create/', AddPostView.as_view(), name='create_post' ),
    path('create/country/', AddCountryView.as_view(), name='create_country' ),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='post-edit'),
    path('post/remove/<int:pk>', DeletePostView.as_view(), name='post-delete'),
    path('country/<str:cont>/', CountryView, name='country'),
    path('country/list', CountryListView, name='country-list'),
    path('like/<int:pk>', LikeView, name='like_post' ),
    path('dislike/<int:pk>', DislikeView, name='dislike_post'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='create_comment' ),


]
