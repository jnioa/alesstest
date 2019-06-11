from django.http import HttpResponse

def index(request):
    str_out = ""
    str_out += "次のリンク先では三種類の宇宙人に関する文章が表示されます。<p />"
    str_out += "学籍番号が奇数の方は上のリンクを、偶数の方は下のリンクを開いて文章を記憶してください。<p />"
    str_out += "制限時間は90秒で、90秒後に自動的に次のページに移ります。<p />"
    str_out += "そのページにあるリンクを5分後にクリックし、問題を解いてください。<p />"
    str_out += "奇数    :"
    str_out += "<a href='alesstest/'>start</a><p />"
    str_out += "偶数    :"
    str_out += "<a href='hard/'>start</a><p />"
    return HttpResponse(str_out)
