from django.shortcuts import render
from scone.scripts.scraper import scrape
from django.shortcuts import render
from django.http import HttpResponse
from scone.models import Companyy
from scone.scripts.randomMetrics import alg

def fakeurl(request):



    return render(request, 'base.html')

def work(request):
    if request.method == 'POST':
    # Process the form data
        namee = request.POST.get('companySearch')
        two, three, env, soc, ticket = scrape(namee)

        FS, EV, NH, TR = alg(env, soc, three)


        company = Companyy(name=namee, symbol=ticket, FS=FS, EV=EV, CT=TR )
        company.save()

        obj = Companyy.objects.first()

        print(obj.FS)


        





        context = {
            'two': two,
            'three': three
        }
    else:
        context = {
            'one': 1,
        }
    



    return render(request, 'graph.html', context)
# Create your views here.
