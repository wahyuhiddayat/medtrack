from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Wahyu Hidayat',
        'class': 'PBP A'
        # nanti tambahin lagi sesuai checklist
    }

    return render(request, "main.html", context)
