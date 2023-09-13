<h1>Medtrack><h1>

<h3>Nama    : Wahyu Hidayat<h3>
<h3>NPM     : 2201233210<h3>
<h3>Kelas   : PBP A<h3>

<h3>Adaptable : https://medtrack.adaptable.app/main<h3><br>

## Membuat Sebuah Proyek Django Baru ##
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

## Membuat Aplikasi Dengan Nama `main` Pada Proyek ##
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

## Melakukan Routing Pada Proyek Agar Dapat Menjalankan Aplikasi `main` ##
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

## Membuat Model Pada Aplikasi `main` Dengan Nama `Item` dan Memiliki Atribut ##
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

## __Deployment__ ke Adaptable ##
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

## Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html` ## 

![bagan client ke web berbasis django dan responnya](https://github.com/wahyuhiddayat/medtrack/blob/main/DjangoMVTArchitecture.png)

1. User mengirim `request` yang mana akan ditangani oleh `controller` (`view.py`).
2. `views.py` akan mengirim `QuerySets` kepada `Models` untuk diproses.
3. Database akan melakukan operasi _Read_ dari `Models`, dan kemudian melakukan operasi _Write_ untuk memperbarui `Models`.
4. `models.py` akan mengirimkan `ResultSet` ke `views.py`.
5. `views.py` akan menampilkan respons ke `Templates` untuk ditampilkan kepada pengguna.


## Mengapa __Virtual Environment__ Digunakan ##
__Virtual environment__ digunakan karena memiliki kemampuan untuk menjaga isolasi antara __package__ dan __dependencies__ dari aplikasi kita. Ini menghindari potensi konflik dengan versi lain yang mungkin ada di sistem komputer kita. Dengan demikian, kita dapat dengan mudah bekerja pada berbagai proyek yang menggunakan versi berbeda tanpa khawatir mengenai konflik. Selain itu, penggunaan __virtual environment__ membantu dalam manajemen proyek dengan lebih baik. Lebih lanjut, dengan mengizinkan kita untuk menggunakan hanya __package__ dan __library__ yang benar-benar diperlukan, __virtual environment__ juga meningkatkan efisiensi sumber daya proyek kita, menghindari penggunaan yang tidak perlu dari seluruh __library__ yang tersedia.

## Memahami Pola Arsitektur Perangkat Lunak: MVC, MVT, MVVM ##

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


