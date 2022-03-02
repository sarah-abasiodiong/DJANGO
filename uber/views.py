from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("""<h1>welcome Sarah ! </h1>
    <br>  <h2>We are happy to have you here on Uber</h2>""")


def about(request):
    return HttpResponse("""<h2>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Minima, tempore, rem consequuntur et sequi temporibus itaque accusantium facere dolores vitae reiciendis aliquid deserunt harum obcaecati consectetur facilis odit modi eligendi!</h2>""")


def order(request):
    return HttpResponse("""<h2>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Minima, tempore, rem consequuntur et sequi temporibus itaque accusantium facere dolores vitae reiciendis aliquid deserunt harum obcaecati consectetur facilis odit modi eligendi!</h2>""")


def booking(request):
    return HttpResponse("""<h2>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Minima, tempore, rem consequuntur et sequi temporibus itaque accusantium facere dolores vitae reiciendis aliquid deserunt harum obcaecati consectetur facilis odit modi eligendi!</h2>""")


def contact(request):
    return HttpResponse("""<h2>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Minima, tempore, rem consequuntur et sequi temporibus itaque accusantium facere dolores vitae reiciendis aliquid deserunt harum obcaecati consectetur facilis odit modi eligendi!</h2>""")












# Create your views here.
