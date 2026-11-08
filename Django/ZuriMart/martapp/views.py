from django.core.exceptions import ValidationError
from django.shortcuts import render

from .models import ContactMessage

REQUIRED_CONTACT_FIELDS = ['first_name', 'last_name', 'email', 'dob', 'gender']


# Create your views here.
def about(request):
    return render(request, 'about.html')


def contacts(request):
    context = {}
    if request.method == 'POST':
        data = request.POST
        context['data'] = data
        missing = [f for f in REQUIRED_CONTACT_FIELDS if not data.get(f, '').strip()]
        if missing:
            context['error'] = 'Please fill in all required fields.'
        else:
            message = ContactMessage(
                first_name=data['first_name'].strip(),
                last_name=data['last_name'].strip(),
                email=data['email'].strip(),
                tel=data.get('tel', '').strip(),
                fax=data.get('fax', '').strip(),
                mob=data.get('mob', '').strip(),
                dob=data['dob'],
                gender=data['gender'],
                comment=data.get('comment', '').strip(),
            )
            try:
                message.full_clean()
            except ValidationError:
                context['error'] = 'Please check your details and try again.'
            else:
                message.save()
                context['success'] = True
    return render(request, 'contact.html', context)


def index(request):
    return render(request, 'index.html')


def services(request):
    return render(request, 'services.html')


def subscribe(request):
    return render(request, 'subscribe.html')
