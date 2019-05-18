from django.shortcuts import render

from .models import RawData


# Create your views here.
def index(request):
    # スタブにするならこっちの形がいい
    # latest_data = RawData.objects.order_by('-time')[:5]
    # template = loader.get_template('portal/index.html')
    # context = {
    #     'latest_data': latest_data,
    # }
    # return HttpResponse(template.render(context, request))

    latest_data = RawData.objects.order_by('-time')[:5]
    context = {
        'latest_data': latest_data,
    }
    return render(request, 'portal/index.html', context)


def detail(request, date):
    pass

