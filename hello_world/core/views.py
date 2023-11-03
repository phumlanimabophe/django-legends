from django.shortcuts import render

def index(request):
    context = {
<<<<<<< HEAD
        "title": "Django example",
    }
    return render(request, "index.html", context)
=======
        "request": request,
        "two_plus_two":2+2
    }
    return render(request, "html_file2.html", context)
>>>>>>> 4a5cfd9 (m)
