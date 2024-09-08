from django.shortcuts import render
def show_main(request):
    context = {
        'name' : 'Old Book',
        'price': 'Rp259.000,00',
        'description': 'Old book found at my backyard'
    }

    return render(request, "main.html", context)
