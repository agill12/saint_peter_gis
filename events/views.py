from django.shortcuts import render,get_object_or_404
from events.models import Event
# Create your views here.
def event_detail(request,id):
    event=get_object_or_404(Event,pk=id)
    event.read=True
    event.views+=1
    event.save()
    
    return render(request, "events/event.html",{'event':event})