Nama    : Wahyu Hidayat<br>
NPM     : 2201233210<br>
Kelas   : PBP A

Adaptable : https://medtrack.adaptable.app

# Step Mengimplementasikan #

## Membuat Sebuah Proyek Django Baru ##
1. Buat direktori baru dengan nama `medtrack`.
2. Masuk ke dalam direktori tersebut dan buka _Terminal_.
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
9. Jalankan server Django dengan perintah berikut (pastikan berkas `manage.py` ada di direktori yang aktif pada `terminal`)
```bash
./manage.py runserver
```
10. Buka http://localhost:8000/ untuk melihat apakah Django berhasil dibuat atau tidak.