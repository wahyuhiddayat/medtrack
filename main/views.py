from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'user': 'Wahyu Hidayat',
        'class': 'PBP A',
        'name': 'Stethoscope',
        'category': "Medical Equipment",
        'amount' : 10,
        'price' : 2000000,
        'description': 'A medical tool used by healthcare professionals to listen to internal body sounds such as heartbeats and respiration.'
    }

    return render(request, "main.html", context)
