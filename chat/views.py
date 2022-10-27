from django.shortcuts import render
from .models import Message

def index(request):
    if request.method == "POST":
        message = Message()
        message.user = request.POST.get("user")
        message.message = request.POST.get("text")
        message.save()
    last_ten = Message.objects.order_by("id")[:10]
    data = Message.objects.all()
    return render(request, "index.html", {'messages':last_ten})


def view_all_messages(request):
    data = Message.objects.all()
    return render(request, "index.html", {'messages': data})