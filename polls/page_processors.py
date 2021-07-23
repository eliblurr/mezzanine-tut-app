
from django.shortcuts import get_object_or_404
from mezzanine.pages.page_processors import processor_for 
from .models import Poll

@processor_for(Poll)
def poll_form(request, page):
    if request.method == "POST":
        p = get_object_or_404(Poll, pk=page.poll.id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except:
        return {'error_message': "You didn't select a choice."}
    else:
        selected_choice.votes += 1 
        selected_choice.save()
        return {'success_message': "Thank you for your vote."}