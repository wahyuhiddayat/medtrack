# 💊 Medtrack 🩺 #


Nama : Wahyu Hidayat <br>
NPM : 2206081894 <br>
Kelas : PBP A 

## ##

## Weekly Assignment ## 

<details>
<summary>Tugas 2</summary>
<br>

# <span id="tugas-2">Tugas 2</span> #

## Contents ## 
- [Membuat Sebuah Proyek Django Baru](#tugas-2-1) 
- [Membuat Aplikasi Dengan Nama `main` Pada Proyek](#tugas-2-2)
- [Melakukan Routing Pada Proyek Agar Dapat Menjalankan Aplikasi `main`](#tugas-2-3) 
- [Membuat Model Pada Aplikasi `main` Dengan Nama `Item` dan Memiliki Atribut](#tugas-2-4) 
- [_Deployment_ ke Adaptable](#tugas-2-5)
- [Bagan Django](#tugas-2-6)
- [Mengapa _Virtual Environment_ Digunakan](#tugas-2-7)
- [MVC, MVT, dan MVVM](#tugas-2-8)

## <span id="tugas-2-1">Membuat Sebuah Proyek Django Baru</span> ##

1. Buat direktori baru dengan nama `medtrack`.
2. Masuk ke dalam direktori tersebut dan buka `Terminal`.
3. Buat __virtual environment__ dengan menjalankan perintah berikut.
```bash
python -m venv env
```
4. Aktifkan __virtual environment__ dengan perintah berikut.
```bash
source env/bin/activate
```
5. Buat berkas `requirements.txt` di direktori yang sama dan tambahkan __dependencies__
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
6. Pasang __dependencies__ dengan perintah berikut (pastikan __virtual environment__ dalam keadaan aktif)
```bash
pip install -r requirements.txt
```
7. Buat proyek Django bernama `medtrack` dengan perintah berikut.
```bash
django-admin startproject medtrack .
```
8. Buka `settings.py` dan tambahkan `*` pada `ALLOWED_HOSTS`
```python
...
ALLOWED_HOSTS = ["*"]
...
```
9. Jalankan server Django dengan perintah berikut (pastikan berkas `manage.py` ada di direktori yang aktif pada `Terminal`)
```bash
./manage.py runserver
```
10. Buka http://localhost:8000/ untuk melihat apakah Django berhasil dibuat atau tidak.
11. Buat repositori GitHub baru bernama `medtrack`.
12. Inisiasi direktori `medtrack` sebagai repositori Git.
13. Tambahkan berkas `.gitignore` pada direktori lokal `medtrack` dan isi berkas dengan:
```
# Django
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media

# Backup files
*.bak 

# If you are using PyCharm
# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# AWS User-specific
.idea/**/aws.xml

# Generated files
.idea/**/contentModel.xml

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# File-based project format
*.iws

# IntelliJ
out/

# JIRA plugin
atlassian-ide-plugin.xml

# Python
*.py[cod] 
*$py.class 

# Distribution / packaging 
.Python build/ 
develop-eggs/ 
dist/ 
downloads/ 
eggs/ 
.eggs/ 
lib/ 
lib64/ 
parts/ 
sdist/ 
var/ 
wheels/ 
*.egg-info/ 
.installed.cfg 
*.egg 
*.manifest 
*.spec 

# Installer logs 
pip-log.txt 
pip-delete-this-directory.txt 

# Unit test / coverage reports 
htmlcov/ 
.tox/ 
.coverage 
.coverage.* 
.cache 
.pytest_cache/ 
nosetests.xml 
coverage.xml 
*.cover 
.hypothesis/ 

# Jupyter Notebook 
.ipynb_checkpoints 

# pyenv 
.python-version 

# celery 
celerybeat-schedule.* 

# SageMath parsed files 
*.sage.py 

# Environments 
.env 
.venv 
env/ 
venv/ 
ENV/ 
env.bak/ 
venv.bak/ 

# mkdocs documentation 
/site 

# mypy 
.mypy_cache/ 

# Sublime Text
*.tmlanguage.cache 
*.tmPreferences.cache 
*.stTheme.cache 
*.sublime-workspace 
*.sublime-project 

# sftp configuration file 
sftp-config.json 

# Package control specific files Package 
Control.last-run 
Control.ca-list 
Control.ca-bundle 
Control.system-ca-bundle 
GitHub.sublime-settings 

# Visual Studio Code
.vscode/* 
!.vscode/settings.json 
!.vscode/tasks.json 
!.vscode/launch.json 
!.vscode/extensions.json 
.history
```
14. `add`, `commit`, dan `push` direktori tersebut ke GitHub.

## <span id="tugas-2-2">Membuat Aplikasi Dengan Nama `main` Pada Proyek</span> ##
1. Jalankan perintah berikut untuk membuat aplikasi baru (pastikan `Terminal` berjalan dengan `medtrack` sebagai direktori yang aktif).
```bash
python manage.py startapp main
```
2. Direktori `main` akan terbentuk dan berisi struktur awal untuk aplikasi.
3. Daftarkan aplikasi `main` ke dalam proyek.
    - Buka berkas `settings.py` di dalam direktori proyek `medtrack`.
    - Tambahkan `main` ke dalam variabel `INSTALLED_APPS`
    ```python
    INSTALLED_APPS = [
        ...,
        'main',
        ...
    ]
    ``` 

## <span id="tugas-2-3">Melakukan Routing Pada Proyek Agar Dapat Menjalankan Aplikasi `main`</span> ##
1. Buat berkas `urls.py` di dalam direktori `main`.
2. Isi `urls.py` dengan kode berikut:
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
3. Buka berkas `urls.py` di dalam direktori proyek `medtrack` (bukan yang di dalam direktori aplikasi `main`).
4. Impor fungsi `include` dari `django.urls`.
```python
...
from django.urls import path, include
...
```
5. Tambahkan rute URL berikut untuk mengarahkan ke tampilan `main` di dalam variabel `urlpatterns`.
```python
urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
```

## <span id="tugas-2-4">Membuat Model Pada Aplikasi `main` Dengan Nama `Item` dan Memiliki Atribut</span> ##

1. Buka berkas `models.py` pada direktori aplikasi `main`.
2. Isi berkas `models.py` dengan kode berikut.
```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)  
    amount = models.IntegerField()           
    description = models.TextField()         
    price = models.IntegerField()            
    date_added = models.DateField(auto_now_add=True)
    category = models.TextField()        
```
- `name` sebagai nama __item__ dengan tipe `CharField`.
- `amount` sebagai jumlah __item__ dengan tipe `IntegerField`.
- `description` sebagai deskripsi __item__ dengan tipe `TextField`.
- `price` sebagai harga __item__ dengan tipe `IntegerField`.
- `date_added` sebagai tanggal __item__ dengan tipe `DateField`.
- `category` sebagai kategori __item__ dengan tipe `TextField`.

## Membuat Sebuah Fungsi Pada `views.py` Untuk Dikembalikan ke Dalam Sebuah __Template__ HTML ##
1. Buka berkas `views.py` yang terletak di dalam berkas aplikasi `main`.
2. Tambahkan bairs impor berikut di bagian paling atas berkas.
```python
from django.shortcuts import render
```
3. Tambahkan fungsi `show_main` berikut:
```python
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
```
4. Buat direktori baru bernama `templates` di dalam direktori aplikasi `main`.
5. Di dalam direktori `templates`, buat berkas baru bernama `main.html` dengan isi sebagai berikut.
```html
<h1>Medtrack</h1>

<h5>Name: </h5>
<p>{{ user }}</p>
<h5>Class: </h5>
<p>{{ class }}</p>

<h4>Name: </h4>
<p>{{ name }}</p>
<h4>Amount: </h4>
<p>{{ amount }}</p>
<h4>Price: </h4>
<p>Rp.{{ price }}</p>
<h4>Category: </h4>
<p>{{ category }}</p>
<h4>Description: </h4>
<p>{{ description }}</p>
```

## <span id="tugas-2-5">_Deployment_ ke Adaptable</span> ##
1. Login menggunakan GitHub di [Adaptable.io](https://adaptable.io/)
2. Tekan tombol `New App` lalu pilih `Connect an Existing Repository`.
3. Hubungkan [Adaptable.io](https://adaptable.io/) dengan GitHub dan pilih `All Repositories` pada proses instalasi.
4. Pilih repositori proyek `medtrack` sebagai basis aplikasi yang akan di-__deploy__.
5. Pilih branch `main` sebagai `deployment branch`.
6. Pilih `Python App Template` sebagai template deployment.
7. Pilih `PostgreSQL` sebagai tipe basis data yang akan digunakan.
8. Cek versi Python menggunakan `Terminal`
    ```bash
    python3 --version
    ```
    didapat output berikut:
    ```
    Python 3.10.6
    ```
9. Isi 3.10 sebagai versi Python.
10. Pada bagian `Start Command` masukkan perintah `python manage.py migrate && gunicorn medtrack.wsgi`.
11. Masukkan `migrate` sebagai nama aplikasi.
12. Centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai proses __deployment__ aplikasi.

## <span id="tugas-2-6">Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`</span> ##

![Django MCT Architecture](https://github.com/wahyuhiddayat/medtrack/blob/main/images/DjangoMVTArchitecture.png)

1. User mengirim `request` yang mana akan ditangani oleh `controller` (`view.py`).
2. `views.py` akan mengirim `QuerySets` kepada `Models` untuk diproses.
3. Database akan melakukan operasi _Read_ dari `Models`, dan kemudian melakukan operasi _Write_ untuk memperbarui `Models`.
4. `models.py` akan mengirimkan `ResultSet` ke `views.py`.
5. `views.py` akan menampilkan respons ke `Templates` untuk ditampilkan kepada pengguna.


## <span id="tugas-2-7">Mengapa _Virtual Environment_ Digunakan</span> ##

_Virtual environment_ digunakan karena memiliki kemampuan untuk menjaga isolasi antara _package_ dan _dependencies_ dari aplikasi kita. Ini menghindari potensi konflik dengan versi lain yang mungkin ada di sistem komputer kita. Dengan demikian, kita dapat dengan mudah bekerja pada berbagai proyek yang menggunakan versi berbeda tanpa khawatir mengenai konflik. Selain itu, penggunaan _virtual environment_ membantu dalam manajemen proyek dengan lebih baik. Lebih lanjut, dengan mengizinkan kita untuk menggunakan hanya _package_ dan _library_ yang benar-benar diperlukan, _virtual environment_ juga meningkatkan efisiensi sumber daya proyek kita, menghindari penggunaan yang tidak perlu dari seluruh _library_ yang tersedia.

## <span id="tugas-2-8">MVC, MVT, dan MVVM</span> ##

## 1. MVC (Model View Controller)

Model-View-Controller (MVC) adalah pola arsitektur yang memisahkan sebuah aplikasi menjadi tiga komponen logis utama: Model, View, dan Controller. Setiap komponen ini dibangun untuk menangani aspek pengembangan yang spesifik dalam sebuah aplikasi. MVC adalah salah satu kerangka kerja pengembangan web standar industri yang paling sering digunakan untuk membuat proyek-proyek yang dapat diukur dan dapat diperluas.

- **Model**: Representasi data dan logika bisnis dalam aplikasi. Model mengelola semua operasi yang berkaitan dengan data.

- **View**: Bertanggung jawab untuk menampilkan data kepada pengguna. Ini adalah tampilan grafis atau antarmuka pengguna.

- **Controller**: Menangani interaksi pengguna, menerima input dari pengguna, dan mengarahkan perubahan ke Model atau View yang sesuai.

## 2. MVT (Model View Template)

Django, sebuah kerangka kerja Python untuk membuat aplikasi web, didasarkan pada arsitektur Model-View-Template (MVT). MVT adalah pola desain perangkat lunak untuk mengembangkan aplikasi web.

- **Model**: Serupa dengan konsep Model dalam MVC, mengelola data dan logika bisnis.

- **View**: Bertanggung jawab untuk menampilkan data dan biasanya memiliki elemen-elemen logika tampilan.

- **Template**: Merupakan bagian yang khas dari kerangka kerja Django. Template adalah file yang mendefinisikan tampilan dan cara data ditempatkan di dalamnya.

## 3. MVVM (Model View ViewModel)

MVVM adalah pola arsitektur, yang diciptakan oleh arsitek Microsoft Ken Cooper dan Ted Peters. MVVM (Model-View-ViewModel) secara jelas memisahkan logika bisnis sebuah aplikasi dari antarmuka pengguna. Tujuan utama dari arsitektur MVVM adalah membuat tampilan sepenuhnya independen dari logika aplikasi.

- **Model**: Sama seperti dalam MVC dan MVT, mengelola data dan logika bisnis.

- **View**: Bertanggung jawab untuk menampilkan elemen antarmuka pengguna, tetapi tidak memiliki logika bisnis yang signifikan.

- **ViewModel**: Merupakan perantara antara Model dan View. Ini mengelola tampilan data dan berisi logika yang diperlukan untuk tampilan. ViewModel memungkinkan View untuk tetap terpisah dari Model dan mendorong penggunaan data yang lebih dekat dengan tampilan.
</details>


<details>
<summary>Tugas 3</summary>
<br>

# <span id="tugas-3">Tugas 3</span> #

## Contents ## 
- [Membuat Input `form` Untuk Menambahkan Objek Model](#tugas-3-1)
- [Menambahkan 5 Fungsi `views` Untuk Melihat Objek yang Sudah Ditambahkan Dalam Format HTML, XML, JSON, XML by _ID_, dan JSON by _ID_](#tugas-3-2)
- [Membuat Routing URL Untuk Masing-Masing `views` yang Telah Ditambahkan](#tugas-3-3)
- [Mengakses Kelima URL Menggunakan Postman](#tugas-3-4)
- [Perbedaan Form `POST` dan `GET` dalam Django](#tugas-3-5)
- [Perbedaan XML, JSON, dan HTML dalam Konteks Pengiriman Data](#tugas-3-6)
- [Mengapa JSON Sering Digunakan dalam Pertukaran Data Antara Aplikasi Web Modern](#tugas-3-7)

## <span id="tugas-3-1">Membuat Input `form` Untuk Menambahkan Objek Model</span> ##

1. Jalankan _virtual environment_ dan karena saya menggunakan MacOS maka saya menggunakan command berikut:
    ```bash
    source env/bin/activate
    ```
2. Buka `urls.py` yang ada pada folder `medtrack` dan modifikasi _path_ `main/` menjadi `''` pada `urlpatterns`.

    _Before_
    ```python
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    ]
    ```
    After
    ```python
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    ]
    ```

3. Buat _folder_ `templates` pada root folder.
4. Buat berkas HTML baru bernama `base.html` yang akan berfungsi sebagai _template_ dasar.
    ```html
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta
                name="viewport"
                content="width=device-width, initial-scale=1.0"
            />
            {% block meta %}
            {% endblock meta %}
        </head>

        <body>
            {% block content %}
            {% endblock content %}
        </body>
    </html>
    ```
5. Buka `settings.py` pada subdirektori `medtrack` dan tambahkan kode berikut agar membuat berkas `base.html` terdeteksi sebagai berkas _template_
    ```python
    ...
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini
            'APP_DIRS': True,
            ...
        }
    ]
    ...
    ```
6. Buka berkas `main.html` pada subdirektori `templates` yang ada pada direktori `main` dan ubah isinya.
    ```html
    {% extends 'base.html' %}

    {% block content %}
        <h1>Medtrack</h1>

        <h5>Name:</h5>
        <p>{{name}}</p>

        <h5>Class:</h5>
        <p>{{class}}</p>
    {% endblock content %}
    ```
    > Kode di atas sama saja dengan kode sebelumnya tetapi hanya menggunakan `base.html` sebagai _template_ utama.
7. Buat berkas baru pada direktori `main` dengan nama `forms.py` untuk membuat struktur form yang dapat menerima data produk baru. Tambahkan kode berikut ke dalam berkas `forms.py`.
    ```python
    from django.forms import ModelForm
    from main.models import Item

    class ProductForm(ModelForm):
        class Meta:
            model = Item
            fields = ["name", "price", "description"]
    ```
8. Buka berkas `views.py` yang ada pada folder main dan tambahkan beberapa import berikut pada bagian paling atas.
    ```python
    from django.http import HttpResponseRedirect
    from main.forms import ProductForm
    from django.urls import reverse
    ```
9. Buat fungsi baru dengan nama `create_product` pada berkas tersebut yang menerima parameter request dan tambahkan potongan kode di bawah ini untuk menghasilkan formulir yang dapat menambahkan data produk secara otomatis ketika data di-submit dari form.
    ```python
    def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
    ```
10. Ubahlah fungsi `show_main` yang sudah ada pada berkas `views.py` menjadi seperti berikut.
    ```python
    def show_main(request):
    items = Item.objects.all()

    context = {
        'name': 'Wahyu Hidayat', 
        'class': 'PBP A', 
        'products': items
    }

    return render(request, "main.html", context)
    ```
11. Buka `urls.py` yang ada pada folder `main` dan import fungsi `create_product`
    ```python
    from main.views import show_main, create_product
    ```
12. Tambahkan path _url_ ke dalam `urlpatterns` pada `urls.py` di `main` untuk mengakses fungsi yang sudah di-import pada poin sebelumnya.
    ```python
    path('create-product', create_product, name='create_product'),
    ```
13. Buat berkas HTML baru dengan nama `create_product.html` pada direktori main/templates. Isi `create_product.html` dengan kode berikut.
    ```html
    {% extends 'base.html' %} 

    {% block content %}
    <h1>Add New Item</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Item"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}
    ```
14. Buka `main.html` dan tambahkan kode berikut di dalam {% block content %} untuk menampilkan data produk dalam bentuk _table_ serta tombol "Add New Item" yang akan _redirect_ ke halaman form.

## <span id="tugas-3-2">Menambahkan 5 Fungsi `views` Untuk Melihat Objek yang Sudah Ditambahkan Dalam Format HTML, XML, JSON, XML by _ID_, dan JSON by _ID_</span> ##
### HTML ###
Buka berkas `views.py` pada direktori `main` dan ubah fungsi `show_main` menjadi sebagai berikut untuk menampilkan semua objek `Item`
```python
from main.models import Item

def show_main(request):
    items = Item.objects.all()

    context = {
        'name': 'Wahyu Hidayat', 
        'class': 'PBP A', 
        'products': items
    }

    return render(request, "main.html", context)
```
### XML ###
Buka berkas `views.py` pada direktori `main` dan tambahkan _import_ _HttpResponse_ dan _Serializer_
```python
from django.http import HttpResponse
from django.core import serializers
```
Tambahkan kode berikut:
```python
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
Import fungsi tadi ke `urls.py` pada direktori `main`
```python
from main.views import show_main, create_product, show_xml 
```
Tambahkan path _url_ ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor tadi.
```python
...
path('xml/', show_xml, name='show_xml'), 
...
```
### JSON ###
Buka berkas `views.py` pada direktori `main` dan tambahkan kode berikut
```python
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
Import fungsi tadi ke `urls.py` pada direktori `main`
```python
from main.views import show_main, create_product, show_xml 
```
Tambahkan path _url_ ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor tadi.
```python
...
path('json/', show_json, name='show_json'), 
...
```
### XML _by_ ID ###
Buka berkas `views.py` pada direktori `main` dan tambahkan kode berikut
```python
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
Import fungsi tadi ke `urls.py` pada direktori `main`
```python
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id
```
Tambahkan path _url_ ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor tadi.
```python
path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
```

### JSON _by_ ID ###
Buka berkas `views.py` pada direktori `main` dan tambahkan kode berikut
```python
def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
Import fungsi tadi ke `urls.py` pada direktori `main`
```python
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
```
Tambahkan path _url_ ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor tadi.
```python
path('json/', show_json, name='show_json'), 
```

## <span id="tugas-3-3">Membuat Routing URL Untuk Masing-Masing Views yang Telah Ditambahkan Pada Poin 2</span> ##
Buka `urls.py` pada direktori `main` dan tambahkan kode berikut
```python
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 

urlpatterns = [
    ...
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    ...
    ]
```

## <span id="tugas-3-4">Mengakses Kelima URL Menggunakan Postman</span> ##
### HTML ###
![Postman HTML](https://github.com/wahyuhiddayat/medtrack/blob/main/images/PostmanHTML.png)

### JSON ###
![Postman JSON](https://github.com/wahyuhiddayat/medtrack/blob/main/images/PostmanJSON.png)

### XML ###
![Postman XML](https://github.com/wahyuhiddayat/medtrack/blob/main/images/PostmanXML.png)

### JSON by ID ###
![Postman JSON by ID](https://github.com/wahyuhiddayat/medtrack/blob/main/images/PostmanJSONById.png)

### XML by ID ###
![Postman XML by ID](https://github.com/wahyuhiddayat/medtrack/blob/main/images/PostmanXMLById.png)

## <span id="tugas-3-5">Perbedaan Form `POST` dan `GET` dalam Django</span> ##
1. `POST`
- Digunakan untuk mengumpulkan data dan meng-encode data tersebut untuk dikirimkan ke server.
- Lebih aman untuk melindungi data karena tidak akan diekspos di URL.
- Digunakan untuk request yang mengubah keadaan sistem, seperti request untuk melakukan perubahan di database.
- Data yang dikirim dengan metode POST melewati header HTTP sehingga keamanan bergantung pada protokol HTTP.
- Data tidak terlihat di URL, sehingga tidak disimpan dalam riwayat browser atau log server web.
- Cocok untuk menambahkan data baru (mengirim data dari formulir HTML) ke dalam database.

2. `GET`
- Digunakan untuk mengirim permintaan request ke server untuk mendapatkan data yang ada di database.
- Request parameter dari method GET ditambahkan ke URL.
- Lebih baik tidak digunakan untuk informasi yang sensitif karena request dari GET terlihat di URL, yang dapat membahayakan keamanan.
- Mengumpulkan data menjadi sebuah string untuk membuat URL bersama dengan nilai-nilainya.
- Digunakan untuk permintaan yang tidak mengubah keadaan sistem, seperti formulir pencarian web.

## <span id="tugas-3-6">Perbedaan XML, JSON, dan HTML dalam Konteks Pengiriman Data</span> ##
1. `XML (eXtensible Markup Language)`
- XML adalah bahasa markup yang digunakan untuk mengorganisir dan menyimpan data secara hierarkis.
- XML memiliki aturan ketat terkait dengan sintaksis dan strukturnya, seperti adanya tag pembuka dan penutup untuk setiap elemen data.
- XML digunakan secara luas untuk pertukaran data antara aplikasi yang berbeda, terutama dalam lingkungan di mana struktur data yang kompleks dan metadata diperlukan.

2. `JSON (JavaScript Object Notation)`
- JSON adalah format ringkas untuk merepresentasikan data dalam bentuk objek dan array.
- JSON lebih ringan dan mudah dibaca oleh manusia dibandingkan dengan XML.
- JSON sering digunakan dalam pengembangan web dan aplikasi karena formatnya yang bersahabat dengan bahasa pemrograman seperti JavaScript.

3. `HTML (HyperText Markup Language)`
- HTML adalah bahasa markup yang digunakan untuk membuat struktur halaman web dan menampilkan konten di browser.
- HTML memiliki elemen dan tag yang digunakan untuk mengatur tampilan dan struktur halaman web.
- HTML bukanlah format yang digunakan untuk pertukaran data seperti XML atau JSON, tetapi digunakan untuk menampilkan data secara visual di browser.

## <span id="tugas-3-7">Mengapa JSON Sering Digunakan dalam Pertukaran Data Antara Aplikasi Web Modern</span> ##
1. Ringkas dan Mudah Dibaca
    - JSON memiliki format yang ringkas dan mudah dibaca oleh manusia. Ini membuatnya ideal untuk pertukaran data yang perlu dipahami oleh pengembang atau administrator sistem. Karena strukturnya yang sederhana, JSON seringkali lebih kompak dibandingkan dengan format lain seperti XML, sehingga menghemat bandwidth.

2. _Language-independent_
    - JSON adalah format data yang independen dari bahasa pemrograman, yang berarti dapat digunakan dengan berbagai bahasa pemrograman seperti JavaScript, Python, PHP, dan banyak lainnya. Hal ini memungkinkan aplikasi yang ditulis dalam bahasa yang berbeda untuk berkomunikasi dengan mudah.

3. Integrasi Web
    - JSON sangat cocok untuk aplikasi web karena bahasa JavaScript secara alami mendukung JSON. Ini memungkinkan browser untuk mengurai data JSON dengan mudah, membuatnya ideal untuk komunikasi antara browser dan server, serta dalam penggunaan API web.

4. Struktur Data yang Fleksibel
    - JSON memungkinkan representasi data yang bersarang dan kompleks, yang cocok untuk data yang memiliki hierarki atau hubungan yang rumit. Ini membuatnya sangat fleksibel untuk menggambarkan berbagai jenis data.

5. Mendukung Tipe Data yang Umum
    - JSON mendukung tipe data umum seperti string, angka, boolean, array, dan objek. Hal ini memudahkan untuk menggambarkan berbagai jenis data, termasuk data teks, numerik, tanggal, dan waktu.

6. Dukungan oleh Banyak Library
    - Ada banyak library JSON yang tersedia untuk berbagai bahasa pemrograman, yang memudahkan pengolahan dan penguraian JSON. Ini membuat penggunaan JSON sangat efisien dalam pengembangan aplikasi.

7. Pengembangan API
    - JSON sering digunakan dalam pengembangan API RESTful karena formatnya yang intuitif dan mudah dipahami. Ini memungkinkan aplikasi berkomunikasi dengan mudah melalui permintaan HTTP yang menggunakan JSON sebagai format pertukuran data.

8. Dukungan Browser
    - Hampir semua browser web modern mendukung JSON, yang membuatnya sangat cocok untuk pertukaran data antara browser dan server, seperti dalam pengembangan aplikasi web berbasis JavaScript.
</details>


<details>
<summary>Tugas 4</summary>
<br>

# <span id="tugas-4">Tugas 4</span> #

## Contents ##
- [Mengimplementasikan Fungsi Registrasi](#tugas-4-1)
- [Mengimplementasikan Fungsi Login](#tugas-4-2)
- [Mengimplementasikan Fungsi Logout](#tugas-4-3)
- [Membuat Pengguna untuk Mengakses Aplikasi Sebelumnya dengan Lancar](#tugas-4-4)
- [Membuat Dua Akun Pengguna dengan Masing-masing Tiga _Dummy Data_ Menggunakan `model` yang telah Dibuat pada Aplikasi Sebelumnya untuk Setiap Akun di Lokal](#tugas-4-5)
- [Menghubungkan model Item dengan User](#tugas-4-6)
- [Menampilkan Detail Informasi Pengguna yang Sedang _logged in_ Seperti `username` dan Menerapkan `cookies` Seperti _last login_ pada Halaman Utama Aplikasi](#tugas-4-7)
- [Apa itu `Django UserCreationForm` dan Kelebihan dan Kekurangannya](#tugas-4-8)
- [Apa Perbedaan Antara `Autentikasi` dan `Otorisasi` dalam Konteks `Django`, dan Mengapa Keduanya Penting?](#tugas-4-9)
- [Apa Itu Cookies Dalam Konteks Aplikasi Web, dan Bagaimana Django Menggunakan Cookies Untuk Mengelola Data Sesi Pengguna](#tugas-4-10)
- [Apakah Penggunaan Cookies Aman Secara Default dalam Pengembangan Web, atau Apakah Ada Risiko Potensial yang Harus Diwaspadai?](#tugas-4-11)
- [Bonus](#tugas-4-12)

## <span id="tugas-4-1">Mengimplementasikan Fungsi Registrasi</span> ##
1. Buka `views.py` yang ada pada subdirektori `main` dan buat fungsi dengan nama `register` yang menerima parameter `request`.
    ```python
    def register(request):
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        context = {'form':form}
        return render(request, 'register.html', context)
    ```
2. Tambahkan _import_ `redirect`, `UserCreationForm`, dan `messages` pada bagian paling atas `views.py`.
    ```python
    from django.shortcuts import redirect
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib import messages  
    ```
3. Buat berkas `register.html` pada pada folder `main/templates` lalu isi dengan kode berikut.
    ```html
    {% extends 'base.html' %}

    {% block meta %}
        <title>Register</title>
    {% endblock meta %}

    {% block content %}  

    <div class = "login">
        
        <h1>Register</h1>  

            <form method="POST" >  
                {% csrf_token %}  
                <table>  
                    {{ form.as_table }}  
                    <tr>  
                        <td></td>
                        <td><input type="submit" name="submit" value="Daftar"/></td>  
                    </tr>  
                </table>  
            </form>

        {% if messages %}  
            <ul>   
                {% for message in messages %}  
                    <li>{{ message }}</li>  
                    {% endfor %}  
            </ul>   
        {% endif %}

    </div>  

    {% endblock content %}
    ```
3. Buka `urls.py` pada direktori `main` lalu import fungsi `register` yang sudah dibuat.
    ```python
    from main.views import register
    ```
4. Tambahkan _path url_ ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor tadi.
    ```python
    ...
    path('register/', register, name='register'), 
    ...
    ```

## <span id="tugas-4-2">Mengimplementasikan Fungsi Login</span> ##
1. Buka `views.py` yang ada pada subdirektori `main` dan buat fungsi dengan nama `login_user` yang menerima parameter `request`.
    ```python
    def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:show_main')
            else:
                messages.info(request, 'Sorry, incorrect username or password. Please try again.')
        context = {}
        return render(request, 'login.html', context)
    ```
2. Tambahkan import `authenticate` dan `login` pada bagian paling atas `views.py`.
    ```python
    from django.contrib.auth import authenticate, login
    ```
3. Buat berkas `login.html` pada folder `main/templates` lalu isi dengan kode berikut.
    ```python
    {% extends 'base.html' %}

    {% block meta %}
        <title>Login</title>
    {% endblock meta %}

    {% block content %}

    <div class = "login">

        <h1>Login</h1>

        <form method="POST" action="">
            {% csrf_token %}
            <table>
                <tr>
                    <td>Username: </td>
                    <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                </tr>
                        
                <tr>
                    <td>Password: </td>
                    <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                </tr>

                <tr>
                    <td></td>
                    <td><input class="btn login_btn" type="submit" value="Login"></td>
                </tr>
            </table>
        </form>

        {% if messages %}
            <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}     
            
        Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

    </div>

    {% endblock content %}
    ```
4. Buka `urls.py` pada direktori `main` lalu import fungsi `login_user` yang sudah dibuat.
    ```python
    from main.views import login_user 
    ```
5. Tambahkan _path url_ ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor tadi.
    ```python
    ...
    path('login/', login_user, name='login'),
    ...
    ```

## <span id="tugas-4-3">Mengimplementasikan Fungsi Logout</span> ##
1. Buka `views.py` yang ada pada subdirektori `main` dan buat fungsi dengan nama `logout_user` yang menerima parameter `request`.
    ```python
    def logout_user(request):
        logout(request)
        return redirect('main:login')
    ```
2. Tambahkan import `logout` pada bagian paling atas `views.py`.
    ```python
    from django.contrib.auth import logout
    ```
3. Buat berkas `main.html` pada folder `main/templates` lalu tambahkan kode berikut setelah _hyperlink tag_ untuk _Add New Item_.
    ```python
        ...
    <a href="{% url 'main:logout' %}">
        <button>
            Logout
        </button>
    </a>
    ...
    ```
4. Buka `urls.py` pada direktori `main` lalu import fungsi `logout_user` yang sudah dibuat.
    ```python
    from main.views import logout_user
    ```
5. Tambahkan _path url_ ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor tadi.
    ```python
    ...
    path('logout/', logout_user, name='logout'),
    ...
    ```

## <span id="tugas-4-4">Membuat Pengguna untuk Mengakses Aplikasi Sebelumnya dengan Lancar</span> ##
1. Buka `views.py` pada subdirektori `main` dan tambahkan import `login_required` pada bagian paling atas.
    ```python
    from django.contrib.auth.decorators import login_required
    ```
2. Tambahkan kode `@login_required(login_url='/login')` di atas fungsi `show_main` agar halaman `main` hanya dapat diakses oleh pengguna yang sudah _login_ (terautentikasi).
    ```python
    ...
    @login_required(login_url='/login')
    def show_main(request):
    ...
    ```

## <span id="tugas-4-5">Membuat Dua Akun Pengguna dengan Masing-masing Tiga _Dummy Data_ Menggunakan `model` yang telah Dibuat pada Aplikasi Sebelumnya untuk Setiap Akun di Lokal</span> ##
1. Username "adriano"
![Adriano's Items](https://github.com/wahyuhiddayat/medtrack/blob/main/images/Screenshot%202023-09-26%20at%209.36.54%20PM.png)

2. Username "langit"
![Langit's Items](https://github.com/wahyuhiddayat/medtrack/blob/main/images/Screenshot%202023-09-26%20at%209.37.21%20PM.png)


## <span id="tugas-4-6">Menghubungkan model `Item` dengan `User`</span> ##
1. Buka `models.py` yang ada pada subdirektori `main` dan tambahkan kode berikut:
    ```python
    ...
    from django.contrib.auth.models import User
    ...
    ```
2. Pada model `Item` yang sudah dibuat, tambahkan potongan kode berikut:
    ```python
    class Item(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        ...
    ```
3. Buka `views.py` yang ada pada subdirektori `main`, dan ubah potongan kode pada fungsi `create_product` menjadi sebagai berikut:
    ```python
    def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
    ```
4. Modifikasi fungsi `show_main` menjadi sebagai berikut.
    ```python
    def show_main(request):
        items = Item.objects.filter(user=request.user)

        context = {
            'name': request.user.username,
            ...
    ...
    ```
5. Simpan semua perubahan, dan lakukan migrasi model dengan `python manage.py makemigrations`

## <span id="tugas-4-7">Menampilkan Detail Informasi Pengguna yang Sedang _logged in_ Seperti `username` dan Menerapkan `cookies` Seperti _last login_ pada Halaman Utama Aplikasi</span> ##
1. Buka `views.py` yang ada pada subdirektori `main` dan tambahkan import `HttpResponseRedirect`, `reverse`, dan `datetime`.
    ```python
    import datetime
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    ```
2. Ubah fungsi `login_user` pada __blok__ `if user is not None` menjadi potongan kode berikut. 
    ```python
    ...
    if user is not None:
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main")) 
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    ...
    ```
3. Pada fungsi `show_main`, tambahkan potongan kode `'last_login': request.COOKIES['last_login']` ke dalam variabel `context`.
    ```python
    context = {
        'name': request.user.username,
        'class': 'PBP A', 
        'products': items,
        'last_login': request.COOKIES['last_login'],
    }
    ```
4. Ubah fungsi `logout_user` menjadi seperti potongan kode berikut.
    ```python
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    ```
5. Buka berkas `main.html` dan tambahkan potongan kode berikut.
    ```python
    ...
    <h5>Sesi terakhir login: {{ last_login }}</h5>
    ...
    ```

## <span id="tugas-4-8">Apa itu `Django UserCreationForm` dan Kelebihan dan Kekurangannya</span> ##
`UserCreationForm` adalah impor formulir bawaan yang memudahkan pembuatan formulir pendaftaran pengguna dalam aplikasi web. Dengan formulir ini, pengguna baru dapat mendaftar dengan mudah di situs web Anda tanpa harus menulis kode dari awal.

## Kelebihan dan Kekurangan UserCreationForm Django

| **Kelebihan**                                      | **Penjelasan Kelebihan**                                                                                                 | **Kekurangan**                         | **Penjelasan Kekurangan**                                                                                                                |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------- |----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Siap Pakai                                         | Tidak perlu membuat form pendaftaran dari awal. `UserCreationForm` sudah menyediakan field yang diperlukan.              | Tidak Fleksibel                        | Formulir ini sangat dasar dan mungkin tidak memenuhi kebutuhan spesifik suatu aplikasi.                                                  |
| Validasi Otomatis                                  | Formulir ini memiliki validasi bawaan, seperti memeriksa kesamaan kata sandi dan keberadaan nama pengguna yang sama.     | Tampilan Standar                       | Tampilan dan styling dari UserCreationForm adalah standar Django, memerlukan penyesuaian untuk desain antarmuka pengguna yang kustom.    |
| Integrasi dengan Model User                        | Terintegrasi dengan baik dengan model User yang ada di `django.contrib.auth.models`, memudahkan penyimpanan ke database. | Fungsionalitas Terbatas                | Form ini hanya untuk pembuatan pengguna. Untuk fitur lain seperti aktivasi email harus menambahkan logika sendiri.                       |
| Keamanan                                           | Membantu mencegah masalah keamanan umum, seperti injeksi SQL.                                                            |                                        |                                                                                                                                          |


## <span id="tugas-4-9">Apa Perbedaan Antara `Autentikasi` dan `Otorisasi` dalam Konteks `Django`, dan Mengapa Keduanya Penting?</span> ##
### Autentikasi ###
Autentikasi adalah proses verifikasi identitas pengguna. Dengan kata lain, memastikan bahwa pengguna yang mencoba mengakses suatu sumber daya adalah siapa yang mereka klaim sebagai diri mereka.

Django menyediakan sistem autentikasi bawaan yang memungkinkan pengguna untuk mendaftar, masuk, dan keluar dari aplikasi. Modul ini dapat ditemukan di django.contrib.auth. Dengan bantuan User model dan form seperti `AuthenticationForm` dan `UserCreationForm`, Django mempermudah proses autentikasi pengguna.

### Otorisasi ###
Otorisasi adalah proses penentuan apa yang diperbolehkan dilakukan oleh pengguna yang telah terautentikasi. Ini berkaitan dengan pemberian atau pembatasan hak akses ke sumber daya tertentu berdasarkan identitas atau peran pengguna.

Setelah pengguna berhasil terautentikasi, Django menggunakan sistem izin (_permissions_) untuk menentukan apa yang dapat dan tidak dapat dilakukan oleh pengguna tersebut. Misalnya, seseorang mungkin hanya mengizinkan pengguna dengan status "admin" untuk mengedit atau menghapus postingan blog. Django memungkinkan pengembang untuk mendefinisikan izin khusus pada model dan memeriksa izin tersebut saat mengakses tampilan tertentu.

### Pentingnya Autentikasi dan Otorisasi ###
### Mengapa Autentikasi dan Otorisasi Penting?

| **Aspek**                             | **Penjelasan**                                                                                                                                                                                 |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Keamanan**                          | Autentikasi memastikan bahwa hanya pengguna yang sah yang dapat mengakses aplikasi, sementara otorisasi memastikan bahwa pengguna tersebut hanya dapat melakukan tindakan yang diperbolehkannya. |
| **Kustomisasi Pengalaman Pengguna**   | Dengan membedakan antara pengguna yang berbeda dan apa yang diizinkan mereka lakukan, aplikasi dapat disesuaikan tampilan dan fungsionalitasnya berdasarkan peran dan kebutuhan pengguna.       |
| **Integritas Data**                   | Otorisasi memastikan bahwa hanya pengguna yang berwenang yang dapat melakukan operasi yang mungkin mempengaruhi integritas data, seperti mengedit atau menghapus entri.                        |
| **Pemenuhan Kebijakan dan Ketentuan** | Dalam banyak aplikasi, ada kebutuhan hukum atau kebijakan untuk memastikan bahwa data hanya dapat diakses atau dimodifikasi oleh individu tertentu. Autentikasi dan otorisasi memungkinkan pemenuhan kebijakan ini.   |


## <span id="tugas-4-10">Apa Itu Cookies Dalam Konteks Aplikasi Web, dan Bagaimana Django Menggunakan Cookies Untuk Mengelola Data Sesi Pengguna</span> ##
### Apa Itu Cookies Dalam Konteks Aplikasi Web? ###

Cookies dalam konteks aplikasi web adalah potongan kecil informasi yang disimpan di peramban pengguna oleh server web. Cookies biasanya digunakan untuk mengidentifikasi pengguna, menyimpan preferensi pengguna, atau informasi lain yang perlu diingat antar sesi browsing. Tujuannya adalah untuk memberikan pengalaman yang disesuaikan bagi pengguna. Sebagai contoh, ketika seseorang mengunjungi situs web belanja dan situs tersebut mengingat item yang telah ditambahkan ke keranjang belanja, itu adalah kerja dari cookies.

### Bagaimana Django Menggunakan Cookies Untuk Mengelola Data Sesi Pengguna? ###

Django menyediakan sistem sesi bawaan yang memungkinkan aplikasi untuk menyimpan dan mengambil data sesi spesifik pengguna. Data ini dienkripsi dan aman, dan dapat digunakan untuk menyimpan informasi seperti ID pengguna, preferensi, atau data lain yang harus tetap konsisten di antara berbagai permintaan dari pengguna yang sama.

Secara default, Django menggunakan cookies untuk mengimplementasikan data sesi. Ini bekerja dengan cara menyimpan ID sesi unik dalam cookie di peramban pengguna, yang kemudian dikaitkan dengan data sesi di server. Setiap kali pengguna kembali ke aplikasi, peramban akan mengirimkan cookie ini kembali ke server, memungkinkan Django untuk mengambil data sesi yang sesuai dengan pengguna tersebut.

Dengan menggunakan cookies untuk sesi, Django dapat memastikan bahwa pengalaman pengguna tetap konsisten dan disesuaikan selama mereka berinteraksi dengan aplikasi web. Namun, penting untuk diingat bahwa ada batas ukuran untuk cookies, jadi jika perlu menyimpan banyak data sesi, mungkin perlu mempertimbangkan solusi lain seperti sesi berbasis database yang juga didukung oleh Django.

## <span id="tugas-4-11">Apakah Penggunaan Cookies Aman Secara Default dalam Pengembangan Web, atau Apakah Ada Risiko Potensial yang Harus Diwaspadai?</span> ##

Penggunaan cookies dalam pengembangan web tidak selalu aman secara default. Meskipun cookies dapat menjadi alat yang berguna untuk menyimpan informasi antar sesi pengguna dan mempersonalisasi pengalaman pengguna, ada juga sejumlah risiko keamanan yang dapat muncul jika tidak dikelola dengan benar.

### Risiko Potensial yang Harus Diwaspadai:

| **Risiko**                   | **Penjelasan**                                                                                                                                                                                                                                    |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Intersepsi Cookies**       | Jika situs web tidak menggunakan HTTPS, cookies dapat dengan mudah diintersepsi oleh pihak ketiga selama transmisi. Ini berarti informasi sensitif yang disimpan dalam cookies dapat jatuh ke tangan yang salah.                                 |
| **Cross-site Scripting (XSS)** | Serangan XSS dapat memungkinkan penyerang untuk membaca cookies dari peramban pengguna. Dengan mengakses cookies, penyerang mungkin mendapatkan akses ke sesi pengguna dan informasi lain yang terkait.                                           |
| **Cross-site Request Forgery (CSRF)** | Meskipun bukan serangan langsung terhadap cookies, CSRF memanfaatkan kepercayaan situs terhadap peramban pengguna. Penyerang dapat menipu pengguna untuk melakukan tindakan tertentu tanpa pengetahuannya, memanfaatkan cookies yang aktif. |
| **Cookie Overwriting**       | Jika situs tidak dengan hati-hati menentukan nama cookies, situs lain dapat menulis ulang cookies tersebut, menggantikan nilai aslinya dengan nilai yang berpotensi berbahaya.                                                                    |
| **Perlindungan Insufficient** | Jika cookies menyimpan informasi sensitif tanpa enkripsi atau tanpa penggunaan atribut keamanan seperti `HttpOnly` atau `Secure`, maka data tersebut lebih rentan terhadap kompromi.                                                              |

## <span id="tugas-4-12">Bonus</span> ##
![Bonus Tugas 4](https://github.com/wahyuhiddayat/medtrack/blob/main/static/images/bonus-tugas4.png)

</details>

<details>
<summary>Tugas 5</summary>
<br>

# <span id="tugas-5">Tugas 5</span> #

## Contents ## 
- [Manfaat dan Penggunaan Element Selector](#tugas-5-1)
- [HTML5 Tag](#tugas-5-2)
- [Perbedaan _Margin_ dan _Padding_](#tugas-5-3)
- [Perbedaan _Framework_ CSS Tailwind dan Bootstrap](#tugas-5-4)
- [Menambahkan Bootstrap ke Aplikasi](#tugas-5-5) 
- [Menambahkan Fitur _Edit_ pada Aplikasi](#tugas-5-6)
- [Membuat Fungsi untuk Menghapus Data Produk](#tugas-5-7)
- [Kustomisasi Halaman `login`](#tugas-5-8)
- [Kustomisasi Halaman `register`](#tugas-5-9)
- [Kustomisasi Halaman `main`](#tugas-5-10)
- [Kustomisasi Halaman `add item`](#tugas-5-11)
- [Kustomisasi Halaman `edit item`](#tugas-5-12)



## <span id="tugas-5-1">Manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya</span> ##
Dalam CSS, _selector_ digunakan untuk memilih elemen-elemen HTML yang akan diberi style. 
1. __Universal Selector__
    - Manfaat: Memilih semua elemen di dalam sebuah dokumen.
    - Kapan Menggunakannya: Ketika ingin memberikan style yang sama ke semua elemen.
    - Contoh:
        ```css
        * {
            margin: 0;
            padding: 0;
        }
        ```
2. __Type Selector (Element Selector)__
    - Manfaat: Memilih semua elemen dengan jenis tertentu.
    - Kapan Menggunakannya: Ketika ingin memberikan _style_ kepada semua elemen dengan jenis yang sama, misalnya semua elemen `<h1>` atau semua elemen `<p>`.
    - Contoh:
        ```css
        h1 {
            color: blue;
        }
        ```
3. __Class Selector (.classname)__
    - Manfaat: Memilih semua elemen yang memiliki atribut `class` tertentu.
    - Kapan Menggunakannya: Ketika ingin memberikan style khusus ke sekelompok elemen yang memiliki atribut class yang sama.
    - Contoh:
        ```css
        .highlight {
            background-color: yellow;
        }
        ```
4. __ID Selector (#idname)__
    - Manfaat: Memilih elemen tunggal yang memiliki atribut `id` tertentu.
    - Kapan Menggunakannya: Ketika ingin memberikan style khusus ke satu elemen saja yang memiliki atribut id tertentu.
    - Contoh:
        ```css
        #header {
            background-color: gray;
        }
        ```
5. __Descendant Selector__
    - Manfaat: Memilih elemen berdasarkan hubungan keturunannya.
    - Kapan Menggunakannya: Ketika ingin memberikan style kepada elemen berdasarkan konteksnya dalam struktur HTML.
    - Contoh:
        ```css
        article p {
            color: red;
            }
        ```
6. __Descendant Selector__
    - Manfaat: Memilih elemen berdasarkan hubungan keturunannya.
    - Kapan Menggunakannya: Ketika ingin memberikan style kepada elemen berdasarkan konteksnya dalam struktur HTML.
    - Contoh:
        ```css
        article p {
            color: red;
            }
        ```
        > Hanya elemen `<p>` yang berada di dalam `<article>` yang akan mendapatkan style 👍.
7. __Child Selector (parent > child)__
    - Manfaat: Memilih semua elemen yang secara langsung merupakan anak dari elemen tertentu.
    - Kapan Menggunakannya: Ketika ingin memilih elemen anak langsung dari sebuah elemen induk, tanpa memilih elemen yang bersarang lebih dalam (child).
    - Contoh:
        ```css
        ul > li {
            list-style-type: square;
        }
        ```
        > Hanya `<li>` yang langsung berada di bawah `<ul>` (tanpa adanya `<ol>` atau `<ul>` lain di antaranya) yang akan terpilih 👍.
7. __Attribute Selector__
    - Manfaat: 
        - `[attr]`: Memilih elemen dengan atribut tertentu
        - `[attr=value]`: Memilih elemen dengan nilai atribut tertentu.
    - Kapan Menggunakannya: Ketika ingin memberikan style berdasarkan keberadaan atau nilai dari atribut tertentu.
    - Contoh:
        ```css
        input[type=text] {
            border: 1px solid black;
        }
        ```
8. __Pseudo-classes__
    - Manfaat: Memilih elemen berdasarkan keadaan tertentu, bukan berdasarkan namanya, contohnya `:hover`, `:active`, `:first-child`, `:nth-child()`.
    - Kapan Menggunakannya: Ketika ingin memberikan style berdasarkan keadaan atau urutan elemen.
    - Contoh:
        ```css
        a:hover {
            color: red;
        }

        p:first-child {
            font-weight: bold;
        }
        ```
9. __Pseudo-elements__
    - Manfaat: Membuat seleksi pada bagian tertentu dari elemen, contohnya `::before`, `::after`, `::first-line`, `::first-letter`.
    - Kapan Menggunakannya: Ketika ingin memodifikasi atau menambahkan konten ke bagian tertentu dari elemen.
    - Contoh:
        ```css
        p::first-line {
            font-weight: bold;
        }

        div::before {
            content: "Note: ";
            font-weight: bold;
        }
        ```
10. __Grouping Selector__
    - Manfaat: Menggabungkan selector untuk menerapkan style yang sama ke beberapa elemen.
    - Kapan Menggunakannya: Ketika ingin menerapkan style yang sama ke lebih dari satu selector.
    - Contoh:
        ```css
        h1, h2, h3 {
            font-family: Arial, sans-serif;
        }
        ```
11. __Combination Selectors__
    - Manfaat: Mengkombinasikan beberapa selector untuk menciptakan seleksi yang lebih spesifik.
    - Kapan Menggunakannya: Ketika ingin menargetkan elemen dengan lebih spesifik, Anda bisa menggunakan combination selectors.
    - Contoh:
        ```css
        div + p {
            margin-top: 20px;
        }

        h1 ~ h2 {
            color: green;
        }
        ```

## <span id="tugas-5-2">Jelaskan HTML5 Tag yang kamu ketahui.</span> ##
- `<!DOCTYPE>`: Menentukan tipe dokumen
- `<html>`: Mendefinisikan dokumen HTML
- `<head>`: Berisi metadata/informasi untuk dokumen
- `<title>`: Mendefinisikan judul untuk dokumen
- `<body>`: Mendefinisikan isi dari dokumen
- `<h1>` - `<h6>`: Mendefinisikan judul (heading) di HTML
- `<p>`: Mendefinisikan paragraf
- <`br>`: Memasukkan jeda baris tunggal
- `<hr>`: Mendefinisikan perubahan tematik dalam konten
- `<!--...-->`: Mendefinisikan sebuah komentar
- `<abbr>`: Mendefinisikan sebuah akronim
- `<b>`: Mendefinisikan teks tebal
- `<sub>`: Mendefinisikan teks subskrip
- `<sup>`: Mendefinisikan teks superskrip
- `<form>`: Mendefinisikan sebuah form HTML untuk masukan pengguna
- `<input>`: Mendefinisikan kontrol masukan
- `<textarea>`: Mendefinisikan kontrol masukan multiline (area teks)
- `<button>`: DMendefinisikan tombol yang dapat diklik
- `<label>`: Mendefinisikan label untuk elemen `<input>`
- `<img>`: Mendefinisikan sebuah gambar
- `<audio>`: Mendefinisikan konten suara
- `<video>`: Mendefinisikan video atau film
- `<a>`: Mendefinisikan hyperlink
- `<link>`: Mendefinisikan hubungan antara dokumen dengan sumber eksternal (sering digunakan untuk menghubungkan ke lembar gaya)
- `<nav>`: Mendefinisikan tautan navigasi
- `<ul>`: Mendefinisikan daftar tidak berurutan
- `<ol>`: Mendefinisikan daftar berurutan
- `<li>`: Mendefinisikan item daftar
- `<table>`: Mendefinisikan tabel
- `<th>`: Mendefinisikan sel header dalam tabel
- `<tr>`: Mendefinisikan baris dalam tabel
- `<td>`: Mendefinisikan sel dalam tabel
- `<style>`: Mendefinisikan informasi gaya untuk dokumen
- `<div>`: Mendefinisikan bagian dalam dokumen
- `<span>`: Mendefinisikan bagian dalam dokumen
- `<header>`: Mendefinisikan header untuk dokumen atau bagian
- `<footer>`: Mendefinisikan footer untuk dokumen atau bagian
- `<section>`: Mendefinisikan bagian dalam dokumen
- `<head>`: Mendefinisikan informasi tentang dokumen
- `<meta>`: Mendefinisikan metadata tentang dokumen HTML

## <span id="tugas-5-3">Jelaskan perbedaan antara margin dan padding</span> ##
![Margin and Padding](https://github.com/wahyuhiddayat/medtrack/blob/main/static/images/margin%20vs%20padding.png)

## Perbedaan antara Margin dan Padding

| Aspek                | Margin                                                                                                                     | Padding                                                                                                                    |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| **Lokasi**           | Merupakan ruang di luar batas (border) elemen. Mengatur jarak antara elemen dengan elemen lain di sekitarnya.               | Merupakan ruang di antara konten elemen dan batas (border) elemen tersebut. Mengatur jarak antara konten elemen dengan batas elemen.  |
| **Pengaruh Terhadap Layout** | Dapat menyebabkan elemen saling menjauh atau mendekat, karena mempengaruhi ruang di luar elemen.                         | Tidak mempengaruhi jarak antar elemen, tetapi dapat mempengaruhi ukuran keseluruhan elemen jika tidak menggunakan `box-sizing: border-box`. |
| **Warna Latar Belakang** | Tidak akan mewarisi warna latar belakang dari elemen. Margin selalu transparan.                                            | Mewarisi warna latar belakang dari elemen. Jika elemen memiliki background color, maka padding juga akan menampilkan warna tersebut.       |
| **Collapsing**       | Dapat "collapse". Ini berarti jika dua elemen berurutan memiliki margin vertikal (atas dan bawah), margin terbesar dari keduanya yang akan digunakan, bukan jumlah keduanya. | Tidak pernah "collapse". Padding dari dua elemen yang berdekatan akan selalu ditambahkan bersama.                                    |


## <span id="tugas-5-4">Perbedaan antara framework CSS Tailwind dan Bootstrap</span> ##
Tailwind CSS dan Bootstrap adalah dua framework CSS populer yang sering digunakan oleh pengembang web untuk membangun antarmuka pengguna yang responsif dan menarik. 

1. __Pendekatan Desain__
    - __Tailwind CSS__
        - Mengadopsi pendekatan _utility-first_, di mana kelas utilitas digunakan untuk membangun antarmuka secara bertahap.
        - Menyediakan kebebasan total dalam desain tanpa keterikatan pada desain komponen spesifik.
        - Cenderung membutuhkan kelas tambahan pada elemen untuk mendapatkan tampilan yang diharapkan.
    - __Bootstrap__
        - Memiliki desain yang sudah ditentukan, menyajikan komponen yang telah dirancang sebelumnya.
        - Efisien untuk _prototyping_ dan membangun halaman dengan cepat tanpa perlu desain spesifik.
        - Pendekatan berbasis komponen memungkinkan tampilan yang konsisten dengan upaya minimal.
2. __Ukuran File__
    - __Tailwind CSS__
        - Secara standar memiliki ukuran file yang besar. Tetapi, dengan alat seperti PurgeCSS, ukuran file CSS bisa diperkecil berdasarkan kelas yang digunakan.
    - __Bootstrap__
        - Mencakup ukuran file yang lebih besar akibat beragam komponennya. Namun, Bootstrap menawarkan kemungkinan untuk mengurangi ukuran dengan memilih komponen spesifik saja.
3. __Customisasi__
    - __Tailwind CSS__
        - Menawarkan fleksibilitas tinggi, memudahkan modifikasi konfigurasi sesuai kebutuhan desain.
        - Pendekatan _utility-first_ memberikan kebebasan total dalam menciptakan desain yang unik.
    - __Bootstrap__
        - Bisa disesuaikan, namun terdapat batasan dalam mengubah desain dasar komponen yang sudah tersedia.
        - Desain yang sangat khusus mungkin memerlukan penyesuaian intensif pada komponen atau kelas Bootstrap.

__Kapan Menggunakan Bootstrap daripada Tailwind:__
- Saat kebutuhan membangun prototipe dengan kecepatan tinggi.
- Ketika diperlukan solusi komprehensif yang mencakup komponen desain beserta javascript.
- Jika sudah terbiasa dengan Bootstrap dan mendapati pendekatannya sesuai.

__Kapan Menggunakan Tailwind daripada Bootstrap:__
- Saat keinginan ada pada kebebasan desain tanpa keterbatasan komponen spesifik.
- Ketika pendekatan utility-first lebih disukai dan ada keinginan membangun tampilan dari dasar.
- Saat tujuan adalah menciptakan tampilan yang unik, bukan berdasarkan template Bootstrap.

## <span id="tugas-5-5">Menambahkan Bootstrap ke Aplikasi</span> ##
1. Buka `base.html` pada direktori `templates` di _root project_ dan tambahkan kode berikut.
    ```html
    <head>
        {% block meta %}
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1">
        {% endblock meta %}
    </head>
    ```
    Kode tersebut berfungsi agar halaman web dapat menyesuaikan ukuran dan perilaku perangkat _mobile_.
2. Tambahkan `Bootstrap CSS` dan `JS`.
    ```html
    {% endblock meta %}
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
    ```

## <span id="tugas-5-6">Menambahkan Fitur _Edit_ pada Aplikasi</span> ##
1. Buka `views.py` pada subdirektori `main` dan tambahkan kode berikut:
    ```python
    def edit_product(request, id):
    # Get product berdasarkan ID
    item = Item.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ProductForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
    ```
2. Buat berkas `edit_product.html` pada subdirektori `main/templates` dan isi dengan kode berikut:
    ```html
    {% extends 'base.html' %}

    {% load static %}

    {% block content %}

    <h1>Edit Product</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Edit Product"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}
    ```
3. _Import_ fungsi `edit_product` di `urls.py` pada direktori `main` dan juga tambahkan _path_ url ke dalam `urlpatterns`.
    ```python
    from main.views import edit_product

    ...
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    ...
    ```
4. Buka `main.html` pada subdirektori `main/templates` dan tambahkan kode berikut sejajar dengan elemen `<td>` terakhir untuk memunculkan _button_ _edit_
    ```html
    <td>
        <a href="{% url 'main:edit_product' product.pk %}">
            <button>
                Edit
            </button>
        </a>
    </td>
    ```

## <span id="tugas-5-7">Membuat Fungsi untuk Menghapus Data Produk</span> ##
1. Tambahkan fungsi `delete_product` pada `views.py` di folder `main`
    ```python
    def delete_product(request, id):
        # Get data berdasarkan ID
        item = Item.objects.get(pk = id)
        # Hapus data
        item.delete()
        # Kembali ke halaman awal
        return HttpResponseRedirect(reverse('main:show_main'))
    ```
2. _Import_ fungsi `delete_product` di `urls.py` pada direktori `main` dan juga tambahkan _path_ url ke dalam `urlpatterns`.
    ```python
    from main.views import delete_product

    ...
    path('delete/<int:id>', delete_product, name='delete_product'),
    ...
    ```

## <span id="tugas-5-8">Kustomisasi Halaman `login`</span> ##
Membuat `css` dengan cara menambahkan kode berikut pada `login.html` di direktori `main/templates`.
    ```html
    <style>
        (isi kode CSS)
    </style>
    ```

![Login](https://github.com/wahyuhiddayat/medtrack/blob/main/static/images/login%20preview.png)

## <span id="tugas-5-9">Kustomisasi Halaman `register`</span> ##
Membuat `css` dengan cara menambahkan kode berikut pada `register.html` di direktori `main/templates`.
    ```html
    <style>
        (isi kode CSS)
    </style>
    ```

![Register](https://github.com/wahyuhiddayat/medtrack/blob/main/static/images/register%20preview.png)

## <span id="tugas-5-10">Kustomisasi Halaman `main`</span> ##
Membuat `css` dengan cara menambahkan kode berikut pada `main.html` di direktori `main/templates`.
    ```html
    <style>
        (isi kode CSS)
    </style>
    ```

![Main](https://github.com/wahyuhiddayat/medtrack/blob/main/static/images/main%20page%20preview.png)

## <span id="tugas-5-11">Kustomisasi Halaman `add item`</span> ##
Membuat `css` dengan cara menambahkan kode berikut pada `create_product.html` di direktori `main/templates`.
    ```html
    <style>
        (isi kode CSS)
    </style>
    ```

![Add New Item](https://github.com/wahyuhiddayat/medtrack/blob/main/static/images/add%20new%20item%20preview.png)

## <span id="tugas-5-12">Kustomisasi Halaman `edit item`</span> ##
Membuat `css` dengan cara menambahkan kode berikut pada `edit_product.html` di direktori `main/templates`.
    ```html
    <style>
        (isi kode CSS)
    </style>
    ```

![Edit Item](https://github.com/wahyuhiddayat/medtrack/blob/main/static/images/edit%20product%20preview.png)


</details>
