# 💊 Medtrack 🩺 #

### Nama    : Wahyu Hidayat ###
### NPM     : 2201233210 ###
### Kelas   : PBP A ###

<h3>Adaptable : https://medtrack.adaptable.app/main<h3><br>

## Section ## 
- [Tugas 2](#tugas-2)
    - [Membuat Sebuah Proyek Django Baru](#tugas-2-1) 
    - [Membuat Aplikasi Dengan Nama `main` Pada Proyek](#tugas-2-2)
    - [Melakukan Routing Pada Proyek Agar Dapat Menjalankan Aplikasi `main``](#tugas-2-3) 
    - [Membuat Model Pada Aplikasi `main` Dengan Nama `Item` dan Memiliki Atribut](#tugas-2-4) 
    - [_Deployment_ ke Adaptable](#tugas-2-5)
    - [Bagan Django](#tugas-2-6)
    - [Mengapa _Virtual Environment_ Digunakan](#tugas-2-7)
    - [MVC, MVT, dan MVVM](#tugas-2-8)
- [Tugas 3](#tugas-3)
    - [Membuat Input `form` Untuk Menambahkan Objek Model](#tugas-3-1)
    - [Menambahkan 5 Fungsi `views` Untuk Melihat Objek yang Sudah Ditambahkan Dalam Format HTML, XML, JSON, XML by _ID_, dan JSON by _ID_](#tugas-3-2)
    - [Membuat Routing URL Untuk Masing-Masing `views` yang Telah Ditambahkan](#tugas-3-3)
    - [Mengakses Kelima URL Menggunakan Postman](#tugas-3-4)
    - [Perbedaan Form `POST` dan `GET` dalam Django](#tugas-3-5)
    - [Perbedaan XML, JSON, dan HTML dalam Konteks Pengiriman Data](#tugas-3-6)
    - [Mengapa JSON Sering Digunakan dalam Pertukaran Data Antara Aplikasi Web Modern](#tugas-3-7)


<h1 id="tugas-3" style="color: #FFBF18;">Tugas 3</h1>

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
JSON memiliki format yang ringkas dan mudah dibaca oleh manusia. Ini membuatnya ideal untuk pertukaran data yang perlu dipahami oleh pengembang atau administrator sistem. Karena strukturnya yang sederhana, JSON seringkali lebih kompak dibandingkan dengan format lain seperti XML, sehingga menghemat bandwidth.

2. _Language-independent_
JSON adalah format data yang independen dari bahasa pemrograman, yang berarti dapat digunakan dengan berbagai bahasa pemrograman seperti JavaScript, Python, PHP, dan banyak lainnya. Hal ini memungkinkan aplikasi yang ditulis dalam bahasa yang berbeda untuk berkomunikasi dengan mudah.

3. Integrasi Web
JSON sangat cocok untuk aplikasi web karena bahasa JavaScript secara alami mendukung JSON. Ini memungkinkan browser untuk mengurai data JSON dengan mudah, membuatnya ideal untuk komunikasi antara browser dan server, serta dalam penggunaan API web.

4. Struktur Data yang Fleksibel
JSON memungkinkan representasi data yang bersarang dan kompleks, yang cocok untuk data yang memiliki hierarki atau hubungan yang rumit. Ini membuatnya sangat fleksibel untuk menggambarkan berbagai jenis data.

5. Mendukung Tipe Data yang Umum
JSON mendukung tipe data umum seperti string, angka, boolean, array, dan objek. Hal ini memudahkan untuk menggambarkan berbagai jenis data, termasuk data teks, numerik, tanggal, dan waktu.

6. Dukungan oleh Banyak Library
Ada banyak library JSON yang tersedia untuk berbagai bahasa pemrograman, yang memudahkan pengolahan dan penguraian JSON. Ini membuat penggunaan JSON sangat efisien dalam pengembangan aplikasi.

7. Pengembangan API
JSON sering digunakan dalam pengembangan API RESTful karena formatnya yang intuitif dan mudah dipahami. Ini memungkinkan aplikasi berkomunikasi dengan mudah melalui permintaan HTTP yang menggunakan JSON sebagai format pertukuran data.

8. Dukungan Browser
Hampir semua browser web modern mendukung JSON, yang membuatnya sangat cocok untuk pertukaran data antara browser dan server, seperti dalam pengembangan aplikasi web berbasis JavaScript.


<h1 id="tugas-2" style="color: #FFBF18;">Tugas 2</h1>

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

![bagan client ke web berbasis django dan responnya](https://github.com/wahyuhiddayat/medtrack/blob/main/DjangoMVTArchitecture.png)

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




