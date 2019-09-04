from django.shortcuts import render
# from django.http import HttpResponse

no = 1


# Create your views here.
# def home_page(request):
#     render(request, 'index.html')

def home_page(request):
    global no

    # return HttpResponse('<html><title>To-Do lists</title></html>')
    new_item = request.POST.get('item_text', '')

    if new_item:
        new_item = str(no) + '. ' + new_item
        no += 1

    return render(request, 'home.html',
                  {'new_item_text': new_item})
