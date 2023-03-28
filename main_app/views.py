from django.shortcuts import render
from .models import Cat

# Temporary Data
# cats = [
#   {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
#   {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
#   {'name': 'Kilgore', 'breed': 'ferrel', 'description': 'cuddle bug', 'age': 0},
# ]

# Create your views here:
def home(request):
  return render(request, 'home.html')
def about(request):
  return render(request, 'about.html')
def cats_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', {
    'cats': cats
  })