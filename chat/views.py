from django.shortcuts import render
from .models import Message
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
def index(request):
    if request.method == "POST":
        message = Message()
        message.user = request.POST.get("user")
        message.message = request.POST.get("text")
        message.save()
    last_ten = Message.objects.all()
    return render(request, "index.html", {'messages':last_ten})
@api_view(["GET"])
def get_new_massage(request):
    with open('data.json', 'r') as outfile:
        d = json.load(outfile)
    return Response(d)

@api_view(["GET"])
def get_all_masseges(request):
    objs = Message.objects.all()
    all_messages = {}
    all_messages['user'] = []
    all_messages['message'] = []
    for i in range(objs.count()-2):
        if objs[i].user is None:
            objs[i].user = "Кто-то"
            objs[i].save()
        if objs[i].message is None:
            continue
        if i == 0:
            try:
                all_messages['user'] += [objs[i].user]
                all_messages['message'] += [objs[i].message]
            except:
                all_messages['user'] += ["Кто это?"]
                all_messages['message'] += [objs[i].message]
        else:
            try:
                all_messages['user'] += [objs[i].user]
                all_messages['message'] += [objs[i].message]
            except:
                all_messages['user'] += ["Кто это?"]
                all_messages['message'] += [objs[i].message]
    print(all_messages)
    with open('data_all.json', 'w') as outfile:
        json.dump(all_messages, outfile)
    with open('data_all.json', 'r') as outfile:
        d = json.load(outfile)
    return Response(d)

