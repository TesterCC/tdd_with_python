from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# home_page = None
from lists.models import Item


def home_page(request):

    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])

    # return HttpResponse('<html><title>To-Do lists</title></html>')

    # P61
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
    else:
        new_item_text = ''

    return render(request, 'home.html', {
        'new_item_text': new_item_text,
    })
