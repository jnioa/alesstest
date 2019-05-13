from django.http import HttpResponse

def index(request):
    str_out = ""
    str_out += "aless memorytest<p />"
    str_out += "easy    :"
    str_out += "<a href='alesstest/'>start</a><p />"
    str_out += "hard    :"
    str_out += "<a href='hard/'>start</a><p />"
    str_out += "60秒間で文字列を記憶して下さい<p />"
    return HttpResponse(str_out)
