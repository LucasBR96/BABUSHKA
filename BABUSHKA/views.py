from django.shortcuts import render

def start( request ):
    return render( request , 'base.html' )