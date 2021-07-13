from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def indexHatespeech(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        comments = request.POST.get('comments')

        data = {
            'name' : name,
            'email' : email,
            'subject': subject,
            'comments' : comments,
        }
        comments = '''
        New message: {}
        
        from: {}   
        '''.format(data['comments'], data['email'])
        send_mail(data['subject'], comments, '', ['dev@csis.or.id'])
        return render(request, 'dashboard/dashboard.html', {})