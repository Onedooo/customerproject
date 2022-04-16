from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def customer_list(request):
    name = '장고'
    return HttpResponse('''<h1>Hello Django</h1>
    <p>{name}</p>'''
                        .format(name=name))


def customer_list(request):
    return render(request, 'customer/customer_list.html')
