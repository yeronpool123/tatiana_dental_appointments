from django.shortcuts import render, redirect
from .forms import ClinicalHistoryForm
from .models import ClinicalHistory


from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def add_history(request):
    if request.method == "POST":
        form = ClinicalHistoryForm(request.POST)
        if form.is_valid():
            history = form.save(commit=False)
            history.patient = request.user  # asigna el paciente logueado
            history.save()
            return redirect('view_history')
    else:
        form = ClinicalHistoryForm()
    return render(request, 'history/add_history.html', {'form': form})

def view_history(request):
    histories = ClinicalHistory.objects.filter(patient=request.user)
    return render(request, 'history/view_history.html', {'histories': histories})




@login_required
def dashboard(request):
    return render(request, 'patient/dashboard.html')




