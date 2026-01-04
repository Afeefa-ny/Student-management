from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import AddForm
def update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = AddForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('view')
    else:
        form = AddForm(instance=student)

    return render(request, 'update.html', {'form': form})

def view(request):
    stu = Student.objects.all()
    return render(request, 'view.html', {'stu': stu})

def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')

def add(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view')
    else:
        form = AddForm()

    return render(request, 'add.html', {'form': form})

def delete(request, id):
    stu = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        stu.delete()
        return redirect('view')
    return render(request, 'delete.html', {'stu': stu})