from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView,DetailView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

from django.urls import resolve

from .models import Author,Book,Publisher,Message
from .forms import AuthorForm,PublisherForm,BookForm
from .form_list import get_form



class LoginView(View):
	template_name = 'registration/login.html'
	def get(self,*args,**kwargs):
		if not self.request.user.is_authenticated or not self.request.user.is_active :
			url = self.request.get_full_path()
			print(url)
			return render(self.request,self.template_name)
		else:
			# url = resolve(self.request.path_info).urlname
			url = self.request.get_full_path()
			path = url.split('=')
			# url = self.request.path
			if len(path)>1:
				ur = path[1]
				print(ur)
				return HttpResponseRedirect(ur)
			else: 
				return HttpResponseRedirect('/admins/')


	def post(self,*args,**kwargs):
		username = self.request.POST['username']
		password = self.request.POST['password']
		user = authenticate(self.request,username=username,password=password)
		next = self.request.POST.get('next','/')
		if user is not None:
			login(self.request,user)
			# return HttpResponseRedirect(reverse('admins'))
			return HttpResponseRedirect(next)
		else:
			return HttpResponseRedirect(reverse('login'))


def log_out(request):
	logout(request)
	return HttpResponseRedirect(reverse('login'))


class IndexView(ListView):
	template_name = 'index.html'
	model = Book
	context_object_name = 'boo'

	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data(**kwargs)
		query = Book.objects.all()[:5]
		context['books'] = query
		context['home_active'] = True
		return context


class AuthorList(ListView):
	template_name = 'authors.html'
	model = Author
	context_object_name = 'authors'


class AuthorDetail(DetailView):
	template_name = 'author_detail.html'
	model = Author
	context_object_name = 'author'

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		author = get_object_or_404(Author,pk=self.kwargs['pk'])
		context['book_list'] = Book.objects.filter(author=author)
		return context


class PublisherList(ListView):
	template_name = 'publishers.html'
	model = Publisher
	context_object_name = 'publishers'


class PublisherDetail(DetailView):
	model = Publisher
	context_object_name = 'publisher'
	template_name = 'publisher_detail.html'

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		publisher = get_object_or_404(Publisher,pk=self.kwargs['pk'])
		context['books'] = Book.objects.filter(publisher=publisher)
		return context


# ##############-----------Admin Pages-----------####################

class AdminHomepage(LoginRequiredMixin,ListView):
	template_name = 'admins/admin-index.html'
	model = Publisher
	context_object_name = 'publishers'

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['books'] = Book.objects.all()
		context['authors'] = Author.objects.all()
		return context


class ViewEntries(LoginRequiredMixin,ListView):
	template_name = 'admins/view_entry.html'
	model = Author
	title = None
	context_object_name = 'authors'

	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data(**kwargs)
		context['books'] = Book.objects.all()
		context['publishers'] = Publisher.objects.all()
		context['title'] = self.title
		return context

class Authors(ViewEntries):
	title = 'author'

class Books(ViewEntries):
	title = 'book'

class Publishers(ViewEntries):
	title = 'publisher'



class BooksBy(LoginRequiredMixin,DetailView):
	template_name = 'admins/books_by.html'
	model = Author
	context_object_name = 'author'

	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data(**kwargs)

		author = get_object_or_404(Author,pk=self.kwargs['pk'])
		# print(author)
		query_set = Book.objects.filter(author=author)
		context['books'] = query_set 
		context['authors'] = author
		return context

class Components(View):
	template_name = 'admins/components.html'
	def get(self,*args,**kwargs):
		return render(self.request,self.template_name)



class AdminAddEntry(LoginRequiredMixin,View):
	template_name = 'admins/add-entry.html'
	form = None
	title = None
	def get(self,*args,**kwargs):
		form = get_form(title=self.title,post_data=None)
		context = {'form':form,'title':self.title}
		return render(self.request,self.template_name,context)

	def post(self,*args,**kwargs):
		form = get_form(title=self.title,post_data=self.request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('admins'))
		return render(self.request,self.template_name)


class AddAuthor(AdminAddEntry):
	title = 'author'

class AddBook(AdminAddEntry):
	title = 'book'

class AddPublisher(AdminAddEntry):

	title = 'publisher'


class EditEntry(LoginRequiredMixin,View):
	template_name = 'admins/edit_entry.html'
	model = None
	title = None
	def get(self,*args,**kwargs):
		query = get_object_or_404(self.model,pk=self.kwargs['pk'])
		form = get_form(title=self.title,post_data=None,post_optional=None,initial=query)
		context = {'form':form,'title':self.title}
		return render(self.request,self.template_name,context)

	def post(self,*args,**kwargs):
		form = get_form(title=self.title,post_data=self.request.POST,post_optional=None,initial=None)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('admins'))


class EditPublisher(EditEntry):
	title = 'publisher'
	model = Publisher

class EditAuthor(EditEntry):
	title = 'author'
	model = Author

class EditBook(EditEntry):
	title = 'book'
	model = Book

class ViewDetail(LoginRequiredMixin,DetailView):
	template_name = 'admins/view_detail.html'
	model = None
	title = None

	def get_context_data(self,*args,**kwargs):
		context =  super().get_context_data(**kwargs)
		if self.title == 'author':
			author = get_object_or_404(Author,pk=self.kwargs['pk'])
			books = Book.objects.filter(author=author)
			context['books_len'] = len(books)
			context['books'] = books
			context['title'] = self.title
		elif self.title == 'publisher':
			publisher = get_object_or_404(Publisher,pk=self.kwargs['pk'])
			books = Book.objects.filter(publisher=publisher)
			context['books_len'] = len(books)
			context['books'] = books
			context['title'] = self.title
		else:
			context['title'] = self.title
		return context

class AuthorDetails(ViewDetail):
	title = 'author'
	model = Author

class PublisherDetails(ViewDetail):
	title = 'publisher'
	model = Publisher

class BookDetails(ViewDetail):
	title = 'book'
	model = Book


class Messages(LoginRequiredMixin,View):
	template_name = 'admins/messages.html'
	def get(self,*args,**kwargs):
		return render(self.request,self.template_name)

class ViewMessage(LoginRequiredMixin,DetailView):
	template_name = 'admins/view_message.html'
	model = Message
	context_object_name = 'message'

def read_message(request,id):
	query = get_object_or_404(Message,id=id)
	query.read = True
	query.save()
	my_id=id
	return redirect('view_message',my_id)

# ####################--------End Admin Pages---------###################

class Genre(View):
	template_name = 'genre.html'
	def get(self,*args,**kwargs):
		genre = self.kwargs['name'].upper()
		query = Book.objects.filter(genre=genre)
		context = {'query':query,'banner':True,'genre_active':True}
		return render(self.request,self.template_name,context)

	def post(self,*args,**kwargs):
		form = AuthorForm(self.request.POST)
		if form.is_valid():
			form.save()


class BookDetail(View):
	template_name = 'book-detail.html'
	def get(self,*args,**kwargs):
		query = get_object_or_404(Book,pk=self.kwargs['title'])
		context = {'book':query}
		return render(self.request,self.template_name,context)

	def post(self,*args,**kwargs):
		return render(self.request,self.template_name)



class AllBooks(ListView):
	template_name = 'books.html'
	context_object_name = 'books'
	model = Book

