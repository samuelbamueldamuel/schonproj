from django.shortcuts import render
from scone.scripts.scraper import scrape
from django.shortcuts import render
from django.http import HttpResponse
from scone.models import Company
from scone.scripts.randomMetrics import alg

def fakeurl(request):



    return render(request, 'base.html')

def work(request):
    if request.method == 'POST':
    # Process the form data
        name = request.POST.get('companySearch')
        two, three, env, soc, ticket = scrape(name)

        FS, EV, NH, TR = alg(env, soc, three)


        company = Company(name=name, symbol=ticket, FS=FS, EV=EV, TR=TR )
        company.save()


        





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
