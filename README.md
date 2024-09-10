Web: http://affandi-shafwan-ecommerce.pbp.cs.ui.ac.id/

Langkah-langkah yang dilakukan:
1. Membuat direktori utama, saya menamakannya e-commerce
2. Mengaktifkan virtual environment melalui command prompt
3. Menjalankan perintah di command prompt untuk membuat aplikasi bernama main di dalam proyek e-commerce
4. Mendaftarkan aplikasi main dengan menambahkan 'main' ke variable INSTALLED_APPS di file setting.py
5. Membuat direktori bernama templates didalam aplikasi main, kemudian membuat dan mengisi file main.html
   yang berisi:
   name sebagai nama item dengan tipe CharField,
   price sebagai harga item dengan tipe IntegerField, dan
   description sebagai deskripsi item dengan tipe TextField.
6. Menghubungkan view dengan template dengan cara membuka file views.py di file aplikasi main
7. Kemudian menambahkan fungsi show_main dibawah impor, contoh:
    def show_main(request):
    context = {
        'name' : 'Old Book',
        'price': 'Rp259.000,00',
        'description': 'Old book found in my backyard'
    }
    return render(request, "main.html", context)
8. Modifikasi template, ubah template main.html dengan mengubah name, price, dan 
   description menjadi struktur kode Django yang sesuai untuk menampilkan data. 
   Contoh:
   {{ name }}, {{ price }} dan {{ description }}

9. Mengonfigurasi Routing URL Aplikasi main, dengan mengubah urls.py dengan kode berikut:
   from django.urls import path
   from main.views import show_main
   app_name = 'main'
   urlpatterns = [
    path('', show_main, name='show_main'),
   ]
10. Menambahkan rute URL dalam urls.py proyek untuk menghubungkannya ke tampilan main
11. Buka berkas urls.py di dalam direktori proyek e_commerce, 
    bukan yang ada di dalam direktori aplikasi main. 
12. Lalu menambahkan import, from django.urls import path, include
13. Menambahkan rute url untuk mengarahkan ke tampilan main di dalam variabel urlpatterns
   urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
    ]
14. Berkas urls.py ini bertanggung jawab untuk mengatur rute URL tingkat proyek
15. Menjalankan proyek Django dengan perintah python manage.py runserver
16. Kemudian buka link http://localhost:8000/ di web browser untuk melihat halaman yang sudah dibuat
17. Kemudian membuat proyek baru di pws
18. Pada settings.py di proyek Django yang sudah kamu buat tadi,
    tambahkan URL deployment PWS pada ALLOWED_HOSTS. ...
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "affandi-shafwan-ecommerce.pbp.cs.ui.ac.id"]
19. Setelah mendapatkan Project Credentials dan Project Command, jalankan instruksi project command


**Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**
Check out the live version here: [Layot Store](https://github.com/Affandi21/e-commerce/blob/262a41a2d4b8b37d896adec86daa9672d41f971a/src/IMG_1090.jpg)

**Jelaskan fungsi git dalam pengembangan perangkat lunak!**
1. Git adalah tools yang bersifat open source, sehingga dapat digunakan untuk membuat perangkat lunak secara open source. 
2. untuk kolaborasi dengan banyak orang, kita dapat memanfaatkan Git untuk mengerjakan proyek yang sama (kerja tim). 
3. Sebagai platform fleksibilitas karena dapat digunakan sebagai solusi untuk hosting pada semua proyek. 
4. Sebagai backup, Git dapat dengan mudah mengembalikan ke dalam versi sebelumnya.

**Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**
Karena Django memiliki fitur lengkap ("batteries included"), dokumentasi yang baik, arsitektur terstruktur (MVT), keamanan bawaan, ORM mudah digunakan, dan komunitas besar. Ini memberikan pemahaman menyeluruh tentang pengembangan web serta mendukung skalabilitas dari proyek kecil hingga besar.

**Mengapa model pada Django disebut sebagai ORM?**
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena memungkinkan pengembang untuk berinteraksi dengan database menggunakan objek Python, tanpa perlu menulis kode SQL secara langsung. ORM menghubungkan kelas Python (model) dengan tabel dalam database, sehingga operasi seperti insert, update, delete, dan query dapat dilakukan melalui metode Python yang mudah dipahami, sementara ORM secara otomatis menerjemahkannya menjadi perintah SQL.