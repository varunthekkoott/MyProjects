from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from .models import Mail
from django.urls import reverse
from django.shortcuts import redirect
from json import loads, dumps


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    allow = False
    for i in Mail.objects.all().values():
        if i['username'] == username and i['password'] == password:
            allow = True
            k=i

    if allow:
        return redirect(f'index/{k["id"]}/')

    else:
        return redirect(home)


def pick(request, id):
    template = loader.get_template('pick.html')
    return HttpResponse(template.render({}, request))


def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render({}, request))


def signcheck(request):
    username = request.POST['username']
    password = request.POST['password']
    conf = request.POST['confpass']
    if conf != password:
        return redirect(signup)

    else:
        user = Mail(username=username, password=password)
        user.save()

        return redirect(home)


def inbox(request, id):
    with open('emails.txt', 'r') as file:
        text = file.read()
        mails = loads(text)
    template = loader.get_template('inbox.html')
    current_inbox = mails[id]
    context = {
        'inbox': current_inbox
    }
    return HttpResponse(template.render(context, request))


def mail(request, id, num):  # Not Done
    with open('emails.txt', 'r') as file:
        text = file.read()

    emails = loads(text)
    curr_inbox = emails[id]
    curr_mail = None
    template = loader.get_template('mail.html')
    for i in curr_inbox:
        if i[0] == num:
            curr_mail = i
    if curr_mail == None:
        return inbox(request, id)
    person = curr_mail[1]
    heading = curr_mail[2]
    content = curr_mail[3]
    context = {
        'person': person,
        'heading': heading,
        'content': content
    }

    return HttpResponse(template.render(context, request))


def sendmail(request, id):
    template = loader.get_template('sendmail.html')
    return HttpResponse(template.render({}, request))


def checksendmail(request, id):
    with open('emails.txt', 'r') as file:
        text = file.read()

    data = Mail.objects.get(username=request.POST['person'])
    sender = Mail.objects.get(id=id)
    current_inbox = loads(text)[data['id']]
    try:
        email_id = current_inbox[0][0]
    except IndexError:
        email_id = 0
    current_inbox = current_inbox.insert(0, [email_id, sender['username'], request.POST['heading'], request.POST['content']])
    email_data = loads(text)
    email_data[data['id']] = current_inbox
    email_data = dumps(email_data)
    with open('emails.txt', 'w') as file:
        file.write(email_data)

    return pick(request, id)
