from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import PacienteForm

def adicionar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'adicionar_paciente.html', {'form': form})

def listar_pacientes(request):
    from .models import Paciente
    pacientes = Paciente.objects.all()
    return render(request, 'listar_pacientes.html', {'pacientes': pacientes})



