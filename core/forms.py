from django import forms
from .models import Author,Publisher,Book

class AuthorForm(forms.ModelForm):
	firstname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	lastname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))

	class Meta:
		model = Author
		fields = ['firstname','lastname','date_of_birth']


class PublisherForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	reg_no = forms.CharField(label='Reg No.',widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = Publisher
		fields = ['name','reg_no']


class BookForm(forms.ModelForm):
	GENRE = (
		('MYSTERY','MYSTERY'),
		('THRILLER','THRILLER'),
		('HORROR','HORROR'),
		('ROMANCE','ROMANCE'),
		('FANTASY','FANTASY'),
		('SCI-FI','SCIENCE FICTION'),
		('CRIME','CRIME'),
		('DRAMA','DRAMA')
		)

	title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	author = forms.ModelMultipleChoiceField(queryset=Author.objects.all(),widget=forms.SelectMultiple(attrs={'class':'custom-select'}))
	publisher = forms.ModelChoiceField(queryset=Publisher.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
	genre = forms.ChoiceField(choices=GENRE,widget=forms.Select(attrs={'class':'form-control'}))
	year_published = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))
	size = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	cover = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
	class Meta:
		model = Book
		fields = ('title','cover','author','publisher','genre','year_published','size')

