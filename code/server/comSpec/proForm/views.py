from django.shortcuts import render

# Create your views here.
def mainboard_f(request):
    return render(request, 'forms/pro_form_base.html')

def ram_f(request):
    pass
def graphic_f(request):
    pass
def cpu_f(request):
    pass