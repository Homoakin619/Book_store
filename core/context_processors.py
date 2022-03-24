from .models import Book,Message

def all_messages(request):
	query = Message.objects.all()
	return {'all_messages':query,}

def new_messages(request):
	query = Message.objects.filter(read=False)
	count = query.count()
	return {'new_messages':query,'new_messages_count':count}

def latest_books(request):
	latest_books = Book.objects.all()
	return {'latest_books':latest_books}