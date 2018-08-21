from django.shortcuts import render
import my_first_site
# Create your views here.

from .models import Teacher

def index(request):
    teacher_list = Teacher.objects.all()
    context = {'teacher_list': teacher_list}
    return render(request, 'university/index.html', context)