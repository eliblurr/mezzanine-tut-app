from django.http import HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from .forms import BookForm 
from .models import Author

@processor_for(Author)
def author_form(request, page):
    form = BookForm(initial={'author':page.author})
    if request.method == "POST":        
        form = BookForm(request.POST, request.FILES)
        print( form.is_valid() )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return {"form": form}