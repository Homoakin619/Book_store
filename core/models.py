from django.db import models
from django.urls import reverse

class  Publisher(models.Model):
	name = models.CharField(max_length=80,primary_key=True)
	reg_no = models.CharField(max_length=50)

	def get_absolute_url(self):
		return reverse('publisher-detail',args=(self.name,))

	def __str__(self):
		return self.name

class Author(models.Model):
	firstname = models.CharField(max_length=50,primary_key=True)
	lastname = models.CharField(max_length=50)
	date_of_birth = models.DateField()

	def get_absolute_url(self):
		return reverse('author-detail',args=(self.firstname,))

	def __str__(self):
		return self.firstname +' '+ self.lastname
		

class Book(models.Model):
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
	title = models.CharField(max_length=80,primary_key=True)
	description = models.CharField(max_length=15,null=True)
	cover = models.ImageField()
	author = models.ManyToManyField('Author')
	genre = models.CharField(max_length=15,choices=GENRE)
	publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
	year_published = models.DateField()
	size = models.IntegerField(null=True,blank=True)

	# def get_absolute_url(self):
	# 	return reverse('book-detail',kwargs={'title':self.title})

	def get_absolute_url(self):
		return reverse('book-detail',args=(self.title,))

class Message(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	read = models.BooleanField(default=False)
	time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title