from django.shortcuts import render
from scone.scripts.scraper import scrape
from django.shortcuts import render
from django.http import HttpResponse

def fakeurl(request):



    return render(request, 'base.html')

def work(request):
    if request.method == 'POST':
    # Process the form data
        name = request.POST.get('companySearch')
        two, three = scrape(name)

        context = {
            'two': two,
            'three': three
        }
    else:
        context = {
            'one': 1,
        }
    



    return render(request, 'base.html', context)
# Create your views here.
