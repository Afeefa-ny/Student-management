from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import AddForm   

def update(request, id):
    emp = get_object_or_404(Employee, id=id)   

    if request.method == 'POST':
        form = AddForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect('view')
    else:
        form = AddForm(instance=emp)

    return render(request, 'update.html', {'form': form})

def view(request):
    query = request.GET.get('q')
    
    if query:
        emp = Employee.objects.filter(name__icontains=query)
        
    else:
        emp = Employee.objects.all()

    return render(request, 'view.html', {'emp': emp})

def list(request):
    emp=Employee.objects.all()
    return render(request, 'list.html', {'emp': emp})
def detail(request, id):
    emp = get_object_or_404(Employee, id=id)
    return render(request, 'detail.html', {'emp': emp})
def home(request):
    emp = Employee.objects.all()  
    return render(request, 'home.html', {'employee': emp})
from django.shortcuts import render, get_object_or_404
from .models import Employee


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
    emp = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        emp.delete()
        return redirect('view')
    return render(request, 'delete.html', {'emp': emp})