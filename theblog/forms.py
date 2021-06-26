from django import forms
from .models import Post, Category, Comment

choice_list = []
choices =  Category.objects.all().values_list('name','name')
for item in choices:
	choice_list.append(item)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Blog title'}),
			'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Blog tag'}),
			'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'author', 'type':'hidden'}),
			'header_image': forms.TextInput(attrs={'class':'form-control', 'type':'file'}),
			'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder':'Add Category'}),	
			'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Write Your blog'}),			
			'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Please write a small description about your blog'}),			
		}


class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'category', 'body', 'snippet')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
			'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),			
			'snippet': forms.Textarea(attrs={'class': 'form-control'}),		
		}


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'body')

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),			
			
		}