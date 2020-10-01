from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,'index.html',)

def analyze(request):
    djtext = request.POST.get('text','default')
    #for checkbox value
    removepunc =request.POST.get('RemovePunc','off')
    fullcaps =request.POST.get('fullcaps','off')
    newlineremover =request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc=='on':
        punctuations ='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed =''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext =analyzed
        params ={'purpose':'Remove Punctuations','analyzed_text':analyzed}

    if fullcaps =='on':
        analyzed =''
        for char in djtext:
            analyzed =analyzed+ char.upper()
            djtext =analyzed
        params = {'purpose': 'fully capitalized value', 'analyzed_text': analyzed}

    if newlineremover =='on':
        analyzed =''
        for char in djtext:
            if char!='\n' and char!= '\r':
                analyzed =analyzed+ char
        djtext =analyzed

        params = {'purpose': 'new line remover', 'analyzed_text': analyzed}


    if extraspaceremover =='on':
        analyzed =''
        for index , char in enumerate(djtext):
            if djtext[index] ==' ' and djtext[index+1]==' ':
                pass
            else:
                analyzed =analyzed+ char

        params = {'purpose': 'Space remover', 'analyzed_text': analyzed}
        djtext =analyzed
    if charcount =='on':
        t =0
        for char in djtext:
            t= t+1
        params = {'purpose': 'Character Count', 'analyzed_text': t}




    if (charcount!='on' and extraspaceremover !='on' and removepunc!='on' and newlineremover!='on'and fullcaps!='on'):
        params ={'purpose': 'No utilities is selected', 'analyzed_text': djtext}

    return render(request, 'analyze.html', params)









# def spaceremover(request):
#     return HttpResponse('homejii')
# def charcount(request):
#     return HttpResponse('homehii')
# def capfirst(request):
#     return HttpResponse('homelow')
# def newlineremover(request):
#     return HttpResponse('homeless')