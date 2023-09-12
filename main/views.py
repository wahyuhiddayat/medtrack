from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Wahyu Hidayat',
        'class': 'PBP A',
    }

    #return render(request, "main.html", context)
    return render(request, "main/main.html", context)
