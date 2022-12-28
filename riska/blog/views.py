from django.shortcuts import render
from .forms import ContactForm
from .models import blog
from django.contrib import messages


def hapus_data(request, id_data):
    blogs = blog.objects.filter(id=id_data)
    blogs.delete()

    return redirect('blog')

def ubah_data(request, id_data):
    blogs = blog.objects.get(id=id_data)
    template = 'ubah_data.html'
    if request.POST:
        Form = ContactForm(request.POST, request.FILES, instance=blogs)
        if Form.is_valid():
            Form.save()
            messages.success(request, "data berhasil di update !!!")
            return redirect('ubah_data', id_data=id_data)
    else:
        Form = ContactForm(instance=blogs)
        context = {
            'Form': Form,
            'blogs': blogs,
        }

    return render(request, template, context)


def Data_baru(request):
    if request.POST:
        Form = ContactForm(request.POST, request.FILES)
        if Form.is_valid():
            Form.save()
            Form = ContactForm()
            pesan = "Data Berhasil Diupload"
            context = {
                'Form': Form,
                'pesan': pesan,
            }
            return render(request, 'tambah.html', context)
    else:
        Form = ContactForm()

        context = {
            'Form': Form,
        }

    return render(request, 'tambah.html', context)

def index(request):
    context = {
        'content': 'selamat datang',
    }
    return render(request, 'index.html', context)


def blogs(request):
    blogs = blog.objects.all()

    context = {
        'blogs': blogs,
    }
    return render(request, 'home.html', context)
