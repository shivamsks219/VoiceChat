from django.shortcuts import render
from app import open
from app import voice
import re

ans=""
# Create your views here.
def index(request):
    return render (request, 'index.html')

def submit(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        mode = request.POST.get("mode")
        if mode == "1":
            prompt = voice.sptext()
        if(prompt == -1):
            return render (request, 'index.html')

        res = open.ans(prompt)
        ans = "Here is the result of your question"
        ans += res
        voice.speechtx(ans)
        data = {
            'res': res,
        }
        
        return render (request, 'index.html', data)
    
