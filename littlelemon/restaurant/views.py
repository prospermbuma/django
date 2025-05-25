from django.shortcuts import render
from .forms import BookingForm
from .models import Menu

# VIEWS
# Home view
def home(request):
    return render(request, 'index.html')

# About view
def about(request):
    return render(request, 'about.html')

# Book view
def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Menu view
def menu(request):
    menu_data = Menu.objects.all()
    return render(request, 'menu.html', {'menu': menu_data})

# Menu item
def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, 'menu_item.html', {'menu_item': menu_item})
