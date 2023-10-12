import datetime
import json
from django.forms import ValidationError
#from datetime import datetime
from django.shortcuts import get_object_or_404, render
from main.forms import ProductForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.views.decorators.http import require_http_methods


# Fungsi ini memerlukan pengguna untuk login dan mengembalikan halaman utama dengan konteks yang berisi informasi pengguna dan produk.
@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)  # Mengambil semua item yang berhubungan dengan pengguna yang saat ini login

    # Membuat konteks dengan informasi pengguna dan item yang akan dikirim ke template
    context = {
        'name': request.user.username,  # Username pengguna
        'class': 'PBP A',  # Kelas pengguna (ini statis, mungkin Anda ingin mengambilnya dari profil pengguna)
        'products': items,  # Produk-produk yang dimiliki oleh pengguna
        'last_login': request.COOKIES.get('last_login', 'N/A'),  # Waktu login terakhir pengguna, diambil dari cookie
    }

    # Mengembalikan HTTP response dengan template yang di-render dan konteks yang sudah dibuat
    return render(request, "main.html", context)

# Fungsi ini menangani pembuatan produk baru. Jika form valid, produk akan disimpan ke database.
def create_product(request):
    form = ProductForm(request.POST or None)  # Membuat form instance dengan data yang dikirim oleh pengguna

    # Jika form valid dan metode request adalah POST, simpan data ke database
    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)  # Membuat objek item dari form tetapi belum menyimpannya ke database
        item.user = request.user  # Menetapkan pengguna yang saat ini login sebagai pemilik item
        item.save()  # Menyimpan item ke database
        return HttpResponseRedirect(reverse('main:show_main'))  # Mengalihkan pengguna ke halaman utama

    # Jika form tidak valid, kembalikan form ke template untuk menampilkan pesan kesalahan
    context = {'form': form}
    return render(request, "create_product.html", context)

# Fungsi ini mengembalikan semua data produk dalam format XML.
def show_xml(request):
    data = Item.objects.all()  # Mengambil semua item dari database
    # Mengembalikan data dalam format XML
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# Fungsi ini mengembalikan semua data produk dalam format JSON.
def show_json(request):
    data = Item.objects.all()  # Mengambil semua item dari database
    # Mengembalikan data dalam format JSON
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Fungsi ini mengembalikan data produk tertentu dalam format XML berdasarkan ID produk.
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)  # Mengambil item berdasarkan ID
    # Mengembalikan data dalam format XML
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# Fungsi ini mengembalikan data produk tertentu dalam format JSON berdasarkan ID produk.
def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)  # Mengambil item berdasarkan ID
    # Mengembalikan data dalam format JSON
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Fungsi ini menangani proses registrasi pengguna baru.
def register(request):
    form = UserCreationForm()  # Membuat instance form registrasi baru

    # Jika form telah dikirim dan valid, simpan pengguna baru dan alihkan ke halaman login
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Menyimpan pengguna baru ke database
            messages.success(request, 'Your account has been successfully created!')  # Menampilkan pesan sukses
            return redirect('main:login')  # Mengalihkan pengguna ke halaman login

    # Jika form belum dikirim atau tidak valid, tampilkan form kepada pengguna
    context = {'form':form}
    return render(request, 'register.html', context)

# Fungsi ini menangani proses login pengguna.
def login_user(request):
    if request.method == 'POST':  # Jika metode request adalah POST, proses form login
        username = request.POST.get('username')  # Mendapatkan username dari form
        password = request.POST.get('password')  # Mendapatkan password dari form
        user = authenticate(request, username=username, password=password)  # Otentikasi pengguna

        if user is not None:  # Jika otentikasi berhasil
            login(request, user)  # Log pengguna masuk
            response = HttpResponseRedirect(reverse("main:show_main"))  # Alihkan ke halaman utama
            response.set_cookie('last_login', str(datetime.datetime.now()))  # Setel cookie untuk waktu login terakhir
            return response
        else:  # Jika otentikasi gagal, tampilkan pesan kesalahan
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')

    context = {}
    return render(request, 'login.html', context)  # Tampilkan form login ke pengguna

# Fungsi ini menangani logout pengguna.
def logout_user(request):
    logout(request)  # Log pengguna keluar
    response = HttpResponseRedirect(reverse('main:login'))  # Alihkan ke halaman login
    response.delete_cookie('last_login')  # Hapus cookie untuk waktu login terakhir
    return response

# Menghapus data berdasarkan ID yang diberikan
def delete_data(request, id):
    # Menghapus data berdasarkan ID yang diberikan
    data = Item.objects.get(pk=id)  # Mengambil objek berdasarkan primary key (id)
    data.delete()  # Menghapus objek dari database
    return HttpResponseRedirect(reverse('main:show_main'))  # Mengalihkan pengguna kembali ke halaman utama

# Menaikkan jumlah item (increase)
def increase_amount(request, id):
    if request.method == 'POST':  # Memastikan bahwa metode adalah POST
        data = get_object_or_404(Item, pk=id)  # Menggunakan get_object_or_404 untuk menangani kemungkinan Item tidak ditemukan
        data.amount += 1  # Meningkatkan jumlah barang
        data.save()  # Menyimpan perubahan ke database
        return JsonResponse({"new_amount": data.amount})  # Mengembalikan jumlah baru dalam format JSON
    return HttpResponse(status=400)  # Jika bukan POST, kirim respon 'Bad Request'

# Menurunkan jumlah item (decrease)
def decrease_amount(request, id):
    if request.method == 'POST':  # Memastikan bahwa metode adalah POST
        data = get_object_or_404(Item, pk=id)  # Menggunakan get_object_or_404 untuk menangani kemungkinan Item tidak ditemukan
        if data.amount > 0:
            data.amount -= 1  # Mengurangi jumlah jika lebih dari 0
        else:
            # Respon kesalahan jika jumlah tidak bisa dikurangi
            return JsonResponse({"error": "Cannot decrease, amount is zero"}, status=400)
        data.save()  # Menyimpan perubahan ke database
        return JsonResponse({"new_amount": data.amount})  # Mengembalikan jumlah baru dalam format JSON
    return HttpResponse(status=400)  # Jika bukan POST, kirim respon 'Bad Request'

# Melakukan perubahan (edit) item
def edit_product(request, id):
    item = Item.objects.get(pk=id)  # Mengambil produk berdasarkan ID

    # Membuat form dengan data yang sudah ada dari instance produk
    form = ProductForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":  # Jika form valid dan metode adalah POST
        form.save()  # Menyimpan perubahan pada produk
        return HttpResponseRedirect(reverse('main:show_main'))  # Mengalihkan pengguna kembali ke halaman utama

    context = {'form': form}
    return render(request, "edit_product.html", context)  # Menampilkan form edit dengan data yang sudah ada

# Hapus produk berdasarkan ID, hanya menerima metode DELETE
@require_http_methods(["DELETE"])
def delete_product(request, id):
    item = Item.objects.get(pk=id)
    item.delete()
    return JsonResponse({'status': 'success'})  # Mengembalikan status sukses dalam format JSON

# Mengambil semua produk dan mengembalikannya dalam format JSON
def get_product_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

# Membuat produk baru dari data yang dikirimkan melalui POST 
@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        try:
            name = request.POST.get("name")
            price = request.POST.get("price")
            category = request.POST.get("category")
            description = request.POST.get("description")
            amount = request.POST.get("amount")  # Pastikan ini dikirim dan bukan None
            
            if request.user.is_authenticated:
                user = request.user
            else:
                return JsonResponse({"error": "User not authenticated"}, status=400)

            if not amount:
                return JsonResponse({"error": "Amount is required"}, status=400)

            new_product = Item(name=name, price=price, category=category, description=description, user=user, amount=amount)
            new_product.full_clean()  # validasi model
            new_product.save()

            return HttpResponse(b"CREATED", status=201)
        except ValidationError as e:
            # Tangani kesalahan validasi
            return JsonResponse({"error": e.message_dict}, status=400)
    else:
        return HttpResponseNotFound()