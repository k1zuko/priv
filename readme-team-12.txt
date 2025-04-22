Instalasi wireguard client: https://www.wireguard.com/install/
Tutorial penggunaan wireguard client: https://gist.github.com/faishol01/6cf562acd107d019b631a30c19526bbf

Terdapat dua VPN config yang diberikan kepada setiap tim. Setiap config hanya dapat digunakan oleh satu koneksi pada satu waktu.
Sehingga, satu orang dapat menggunakan satu vpn config untuk terhubung dengan server milik tim.

Satu tim mendapatkan satu buah server. Alamat server tim Anda adalah 10.1.12.10 dengan menggunakan SSH private key yang diberikan.

SSH private key akan diberikan kemudian. Ketika private key sudah dirilis, private key bisa digunakan seperti pada contoh berikut:
ssh -i team-12.pem ubuntu@10.1.12.10

Jika Anda menggunakan Windows, maka kemungkinan besar tidak ada SSH dan hanya ada PuTTY untuk melakukan koneksi ke server.
Perlu diperhatikan bahwa format private key PuTTY menggunakan PPK, sementara private key yang diberikan kepada peserta adalah dalam format PEM.
Peserta dapat melakukan konversi dengan mengikuti tutorial berikut: https://www.puttygen.com/convert-pem-to-ppk

Selamat mengerjakan!
