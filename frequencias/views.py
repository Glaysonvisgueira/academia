from django.shortcuts import render
from frequencias.forms import FrequenciaForm

def realizar_chamada(request):
    context = {}    
    template_name = 'realizar-chamada.html'
    if request.method == "POST":
        form = FrequenciaForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('http://localhost:8000/') 
    else:
        form = FrequenciaForm()
    context['form'] = form
    return render(request, template_name, context)


