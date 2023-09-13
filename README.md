<h1>Medtrack><h1><br>

<h2>Nama    : Wahyu Hidayat<h2>
<h2>NPM     : 2201233210<h2><br>
<h2>Kelas   : PBP A<h2><br>

<h2>Adaptable : https://medtrack.adaptable.app/main<h2><br>

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

class Product(models.Model):
    name = models.CharField(max_length=255)  
    amount = models.IntegerField()           
    description = models.TextField()         
```
- `name` sebagai nama __item__ dengan tipe `CharField`.
- `amount` sebagai jumlah __item__ dengan tipe `IntegerField`.
- `description` sebagai deskripsi __item__ dengan tipe `TextField`.

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
        'name': 'Wahyu Hidayat',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
```
4. Buat direktori baru bernama `templates` di dalam direktori aplikasi `main`.
5. Di dalam direktori `templates`, buat berkas baru bernama `main.html` dengan isi sebagai berikut.
```html
<h1>Medtrack</h1>

<h5>Name: </h5>
<p>{{ name }}<p>
<h5>Class: </h5>
<p>{{ class }}<p>
```
> Sintaks Django {{ name }} dan {{ class }} digunakan untuk menampilkan nilai dari variabel yang telah didefinisikan sebelumnya pada 'show_main'

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

1. User mengirim __request__ yang mana akan ditangani oleh __controller__ (`view.py`).
2. `views.py` akan mengirim `QuerySets` kepada `Models` untuk diproses.
3. Database akan melakukan operasi _Read_ dari `Models`, dan kemudian melakukan operasi _Write_ untuk memperbarui `Models`.
4. `models.py` akan mengirimkan `ResultSet` ke `views.py`.
5. `views.py` akan menampilkan respons ke `Templates` untuk ditampilkan kepada pengguna.


## Mengapa __Virtual Environment__ Digunakan ##
__Virtual environment__ digunakan karena memiliki kemampuan untuk menjaga isolasi antara __package__ dan __dependencies__ dari aplikasi kita. Ini menghindari potensi konflik dengan versi lain yang mungkin ada di sistem komputer kita. Dengan demikian, kita dapat dengan mudah bekerja pada berbagai proyek yang menggunakan versi berbeda tanpa khawatir mengenai konflik. Selain itu, penggunaan __virtual environment__ membantu dalam manajemen proyek dengan lebih baik. Lebih lanjut, dengan mengizinkan kita untuk menggunakan hanya __package__ dan __library__ yang benar-benar diperlukan, __virtual environment__ juga meningkatkan efisiensi sumber daya proyek kita, menghindari penggunaan yang tidak perlu dari seluruh __library__ yang tersedia.

## MVC, MVT, MVVM ##