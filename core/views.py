from django.shortcuts import render, redirect
from .models import Product, Category, Rate
from .forms import EmailForm


def email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or wherever you want
    else:
        form = EmailForm()
    return render(request, 'base.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {'products': products, 'categories': categories})

def contact(request):
    return render(request, 'contact.html')

def menu(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    search = request.Get.get('search')
    rates = Rate.objects.all()
    context = {'products': products, 'categories': categories, 'rates': rates, 'search': search}
    return render(request, 'menu.html', context)


def service(request):
    return render(request, 'service.html')

def blog(request):
    return render(request, 'blog.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')


def shop(request):
    return render(request, 'shop.html')

def thankyou(request):
    return render(request, 'thankyou.html')

def services(request):
    return render(request, 'services.html')



