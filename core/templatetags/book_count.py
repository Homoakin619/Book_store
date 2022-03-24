from django import template
from core.models import Book

register = template.Library()

@register.filter
def get_book(author):
		book = Book.objects.filter(author=author)
		return len(book)

@register.filter
def get_publisher_book(publisher):
		book = Book.objects.filter(publisher=publisher)
		return len(book)