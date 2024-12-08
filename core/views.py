from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group


def index(request):
    return render(request, "core/index.html")

def projects(request):
    return render(request, "core/projects.html")

def resume(request):
    return render(request, "core/resume.html")

#lo de aqui abajo necesita cambiarse por otro archivo que pudiesemos utilizar:
# @login_required
# def products(request):
#     return render(request, 'core/products.html')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user = user_creation_form.save()

            group_name = "Mercancia_Managers"
            group, created = Group.objects.get_or_create(name=group_name)

            if created:
                # Obtener ContentType de Mercancia
                content_type = ContentType.objects.get_for_model(Mercancia)

                # Obtener los permisos asociados al modelo Mercancia
                permissions = Permission.objects.filter(content_type=content_type)

                # Asignar estos permisos al grupo
                group.permissions.set(permissions)

            # Añadir el usuario al grupo
            user.groups.add(group)

            # Autenticar al usuario y redirigir
            login(request, user)
            return redirect('index')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)

# def contact(request):
#     contact_form = ContactForm()
#     if request.metod=='POST':
#         contact_form=contact_form(data=request.POST)
#         if contact_form.is_valid():
#             name=request.post.get('name', '')
#             email=request.POST.get('name','')
#             message=request.POST.get('message','')
#             email=EmailMessage(
#                 'mensaje de contacto recibido',
#                 'mensaje enviado por {} <{}>:\n\n{}'.format(name,email,message),
#                 email,
#                 ['faperezv2004@gmail.com'],
#                 reply_to=[email],
#             )
#             try:
#                 email.send()
#                 return redirect(reverse('contact')+'?error')
#             except:
#                 return redirect(reverse('contact')+'?error')
#     return render(request,'contact/contact.html',{'form':contact_form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            # Get the cleaned data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Prepare the email
            subject = f'New contact form submission from {name}'
            body = f'Name: {name}\nEmail: {email}\nMessage:\n{message}'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.DEFAULT_TO_EMAIL]  # Set this in your settings
            # Send the email
            send_mail(subject, body, from_email, recipient_list)
            # Redirect to a success page or render a success message
            return redirect('contact')  # You can create a success URL or page
    else:
        form = ContactForm()
    
    return render(request, 'core/contact.html', {'form': form})