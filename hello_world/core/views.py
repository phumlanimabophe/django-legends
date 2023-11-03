from django.shortcuts import render

def index(request):
    context = {
        "request": request,
        "two_plus_two":2+2
    }
    return render(request, "html_file2.html", context)
