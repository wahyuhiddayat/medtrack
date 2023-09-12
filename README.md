Nama    : Wahyu Hidayat<br>
NPM     : 2201233210<br>
Kelas   : PBP A

Adaptable : https://medtrack.adaptable.app

# Step Mengimplementasikan #

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