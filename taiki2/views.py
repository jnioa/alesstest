from django.http import HttpResponse

def index(request):
    str_out = ""
    str_out += "5分後にリンクをクリックしてください。<p />"
    str_out += "<a href='https://docs.google.com/forms/d/1MEbvCvjGDmpgnrPuqpvktjqwNaIl904yC44GzFeSXZY/viewform?edit_requested=true'>start</a><p />"
    return HttpResponse(str_out)
