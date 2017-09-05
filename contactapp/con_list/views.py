from rest_framework.viewsets import ModelViewSet
from con_list.serializers import ContactSerializer
from con_list.models import Contact
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from .forms import ContactForm, UserForm



IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


def index(request):
	if not request.user.is_authenticated():
		return render(request, 'login.html')
	else:
		contacts = Contact.objects.filter(user=request.user)
		return render(request, 'index.html' , {'contacts':contacts})



def create_contact(request):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        form = ContactForm(request.POST or None, request.FILES or None)
        contacts = Contact.objects.filter(user=request.user)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            if contact.image:
            	contact.image = request.FILES['image']
            	file_type = contact.image.url.split('.')[-1]
            	file_type = file_type.lower()
            	if file_type not in IMAGE_FILE_TYPES:
                	context = {
                    	'contact': contact,
                    	'form': form,
                    	'error_message': 'Image file must be PNG, JPG, or JPEG',
                	}
                	return render(request, 'create_contact.html', context)
            contact.save()
            return render(request, 'index.html', {'contacts': contacts})
        context = {
            "form": form,
        }
        return render(request, 'create_contact.html', context)






def delete_contact(request, contact_id):
	contacts = Contact.objects.all()
	contact = get_object_or_404(Contact, pk=contact_id)
	contact.delete()
	return render(request, 'index.html', {'contacts': contacts})


def detail(request, contact_id):
	if not request.user.is_authenticated():
		return render(request, 'login.html')
	else:
		user = request.user
		contact = get_object_or_404(Contact, pk=contact_id)
		return render(request, 'detail.html', {'contact': contact, 'user': user})

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                contacts = Contact.objects.filter(user=request.user)
                return render(request, 'index.html', {'contacts': contacts})
    context = {
        "form": form,
    }
    return render(request, 'register.html', context)




def logout_user(request):
	logout(request)
	form = UserForm(request.POST or None)
	context = {
		"form": form,
	}
	return render(request, 'login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                contacts = Contact.objects.filter(user=request.user)
                return render(request, 'index.html', {'contacts': contacts})
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid Credentials!'})
    return render(request, 'login.html')



def favorite(request, contact_id):
	contact = get_object_or_404(Contact, pk=contact_id)
	contacts = Contact.objects.filter(user=request.user)
	try:
		if contact.is_favorite:
			contact.is_favorite = False
		else:
			contact.is_favorite = True
		contact.save()
	except (KeyError, ContactSerializer.DoesNotExist):
		return JsonResponse({'success': False})
	else:
		return render(request, 'index.html', {'contacts':contacts})