from django.shortcuts import render
from .forms import SignUpForm
from .forms import ContactForm

# Create your views here.

def home(request):
    title = 'Welcome'
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form" : form
    }
    if form.is_valid():
        #form.save()
        #print (request.POST['email'])
        instance = form.save(commit = False)
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        # if instance.full_name == None:
        #     instance.full_name == "Guest"
        instance.save()
        context = {
            "title" : "Спасибо за регистрацию."
        }
    return render(request, "home.html", context)



def contact(request):
    title = 'Обратная связь'
    title_align_center = True
    form = ContactForm(request.POST or None)
    if form.is_valid():
        for key, value in form.cleaned_data.items():
            print (key, value)
            #print(form.cleaned_data.get(key))
        # email = form.cleaned_data.get("email")
        # message = form.cleaned_data.get("message")
        # full_name = form.cleaned_data.get("full_name")
        # print(email, message, full_name)

    context = {
        "form" : form,
        "title" : title,
        "title_align_center" : title_align_center
    }
    return render(request, "forms.html", context)








