from django import forms
from .models import Post, Category, Comment

#to hardcode choices
#choices = [(category1, category1 ), (category2, category2 ), (category3, category3 ),]
grades = [('1','1'),('2','2'),('3','3'),('4','4'),('5a','5a'),('5b','5b'),('5c','5c'),
            ('6a','6a'),('6a+','6a+'),('6b','6b'),('6b+','6b+'),('6c','6c'),('6c+','6c+'),('7a','7a'),
            ('7a+','7a+'),('7b','7b'),('7b+','7b+'),('7c','7c'),('7c+','7c+'),('8a','8a'),('8a+','8a+'),
            ('8b','8b'),('8b+','8b+'),('8c','8c'),('8c+','8c+'),('9a','9a'),('9a+','9a+'),('9b','9b'),
            ('9b+','9b+'),('9c','9c'),('9c+','9c+')
]



country = Category.objects.all().values_list('country', 'country').order_by('country')

choice_list = []

for item in country:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_image','title','title_tag', 'country', 'author', 'grades', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of route'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'#Bouldergram'}),
            'country': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'userid', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'grades': forms.Select(choices=grades, attrs={'class': 'form-control'})
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'grades', 'country', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'country': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': 'Country'}),

            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'grades': forms.Select(choices=grades, attrs={'class': 'form-control'})
        }

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': 'Comment'
        }
        widgets = {
            #'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
