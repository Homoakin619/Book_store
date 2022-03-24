from .forms import AuthorForm,PublisherForm,BookForm

def get_form(title,post_data,post_optional=None,initial=None):
    if title == 'author':
        if post_data:
            if initial:
                form = AuthorForm(post_data,instance=initial)
            else:
                form = AuthorForm(post_data)
        else:
            if initial:
                form = AuthorForm(instance=initial)
            else:
                form = AuthorForm()
    if title == 'book':
        if post_data:
            if initial:
                form = BookForm(post_data,post_optional,instance=initial)
            else:
                form = BookForm(post_data)
        else:
            if initial:
                form = BookForm(instance=initial)
            else:
                form = BookForm()
    if title == 'publisher':
        if post_data:
            if initial:
                form = PublisherForm(post_data,instance=initial)
            else:
                form = PublisherForm(post_data)
        else:
            if initial:
                form = PublisherForm(instance=initial)
            else:
                form = PublisherForm()
    return form