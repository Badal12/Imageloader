from django.shortcuts import render
from .forms import ImageForm
from .models import Image

# Create your views here.


def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()  #creating a obj of form
    img = Image.objects.all()  #we have taken that all images into img and we will pass that into templates
    return render(request, 'image_setup/home.html', {'img': img, 'form': form})