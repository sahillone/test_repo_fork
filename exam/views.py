from django.shortcuts import render


def about(request):
    title = {"title": "Exams"}
    return render(request, "exam/index.html", title)
