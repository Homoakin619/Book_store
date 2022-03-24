from django.urls import path,re_path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
# from django.contrib.auth import views as auth_views

from core import views

urlpatterns = [
		path('',views.IndexView.as_view(),name='index'),
		path('genre/<name>',views.Genre.as_view(),name='genre'),
		path('authors/',views.AuthorList.as_view(),name='authors'),
		path('author/<slug:pk>',views.AuthorDetail.as_view(),name='author-detail'),
		path('publishers/',views.PublisherList.as_view(),name='publishers'),
		path('books/',views.AllBooks.as_view(),name='books'),
		path('books/<title>',views.BookDetail.as_view(),name='book-detail'),
		path('add_new_book/',views.AddBook.as_view(),name='new_book'),
		url(r'^publishers/(?P<pk>[-\w.@+*$& -]+)/?$',views.PublisherDetail.as_view(),name='publisher-detail'),

		path('admins/',views.AdminHomepage.as_view(),name='admins'),

		url(r'^admins/authors/edit/(?P<pk>[-\w.@+*$ -]+)/?$',views.EditAuthor.as_view(),name='edit-author'),
		
		path('admins/authors/add_new/',views.AddAuthor.as_view(),name='add-author'),
		path('admins/authors/',views.Authors.as_view(),name='author'),
		url(r'^admins/authors/(?P<pk>[-\w.@+*$ -]+)/?$',views.AuthorDetails.as_view(),name='author_detail'),

		path('admins/books/',views.Books.as_view(),name='books'),
		url(r'^admins/books/edit/(?P<pk>[-\w.@+*$& -]+)/?$',views.EditBook.as_view(),name='edit-book'),
		url(r'^admins/books/(?P<pk>[-\w.@+*$& -]+)/?$',views.BookDetails.as_view(),name='book_detail'),

		url(r'^admins/publishers/(?P<pk>[-\w.@+*$& -]+)/?$',views.PublisherDetails.as_view(),name='publisher_detail'),
		path('admins/publishers/',views.Publishers.as_view(),name='all_publishers'),
		path('admins/publishers/add_new',views.AddPublisher.as_view(),name='add-publisher'),
		url(r'^admins/publishers/edit/(?P<pk>[-\w.@+*$& -]+)/?$',views.EditPublisher.as_view(),name='edit-publisher'),


		path('admins/components/',views.Components.as_view(),name='components'),
		path('admins/messages/',views.Messages.as_view(),name='messages'),
		path('admins/read_message/<int:pk>',views.ViewMessage.as_view(),name='view_message'),
		path('read/<int:id>',views.read_message,name='read'),

		url(r'^admins/authors/(?P<pk>[-\w.@+*$& -]+)/books/',views.BooksBy.as_view(),name='books_by'),
		path('admins/login/',views.LoginView.as_view(),name='logins'),
		path('logout',views.log_out,name='logout'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


