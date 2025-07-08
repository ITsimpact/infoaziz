from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import PageCounter, Skill
from django.contrib import messages

def home(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def skills(request):
    skills = Skill.objects.all()
    total  = PageCounter.objects.filter(path=request.path).first()
    return render(request, "myapp/skills.html", {"skills": skills, "total_hits": total.hits if total else 0})

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        cd = form.cleaned_data
        send_mail(
            subject=f"Новое сообщение от {cd['name']}",
            message=f"Email: {cd['email']}\n\n{cd['message']}",
            from_email=None,
            recipient_list=["sobirjonov0909@gmail.com"],
        )
        messages.success(request, 'Ваше сообщение отправлено!')
        return redirect('contact')

    return render(request, 'myapp/contact.html', {'form': form})

