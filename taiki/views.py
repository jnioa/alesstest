from django.http import HttpResponse

def index(request):
    str_out = ""
    str_out += "5分後にリンクをクリックしてください。<p />"
    str_out += "<a href='https://docs.google.com/forms/d/1CoUGUxYTln1OyMcJD1Ty6uEi7nC-UIaDjzxdOV6ig1E/viewform?pli=1&edit_requested=true'>start</a><p />"
    return HttpResponse(str_out)
