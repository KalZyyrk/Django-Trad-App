from django.shortcuts import render
from translate import Translator

def index(request):
    if request.method == 'POST':
        from_lang = request.POST.get('from_lang')
        to_lang = request.POST['to_lang']
        text = request.POST.get('text')
        translator = Translator(to_lang=to_lang, from_lang=from_lang)
        translate_text = translator.translate(text=text)
        return render(request, 'index.html', {'translate_text': translate_text})
    return render(request, 'index.html')