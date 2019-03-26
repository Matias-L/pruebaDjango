from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponse
from .models import InputForm
from .calcular import compute

def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            return present_output(form)
    else:
        form = InputForm()
    context_instance = RequestContext(request)
    return render(request, 'calculadora1.html', {'form': form})
    #return render_to_response('calculadora1.html', {'form': form}, context_instance)

def present_output(form):
    r = form.r
    s = compute(r)
    return HttpResponse('Hello, World! sin(%s)=%s' % (r, s))