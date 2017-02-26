from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def translate(request):

    original_word = request.GET['original_text']
    new_word = ''
    vowels = 'aeiou'

    for word in original_word.split():
        if word[0].lower() in vowels:
            new_word += word + 'way '
        else:
            new_word += word[1:] + word[0] + 'ay '

    new_word = new_word[:-1]

    return render(request,
                  'translate.html',
                  {'original_word': original_word, 'new_word': new_word})


def about(request):
    from datetime import date
    year, month, day = date.today().timetuple()[0],date.today().timetuple()[1],date.today().timetuple()[2],
    date_string = "{}/{}/{}".format(month,day,year)
    return render(request, 'about.html', {'curr_date':date_string})