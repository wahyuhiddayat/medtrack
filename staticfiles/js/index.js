function addAmount(productId) {
    // Kirim permintaan AJAX ke endpoint yang sesuai untuk menambah jumlah stok
    // Anda dapat menggunakan library seperti jQuery atau fetch API untuk melakukan permintaan AJAX
    // Contoh menggunakan jQuery:
    $.ajax({
        url: '/add_amount/' + productId + '/',
        type: 'POST',
        success: function(response) {
            // Jika permintaan berhasil, perbarui tampilan jumlah stok
            // Misalnya, dengan mengubah teks pada elemen HTML yang sesuai
            $('#amount-' + productId).text(response.amount);
        },
        error: function(xhr, status, error) {
            // Tangani kesalahan jika permintaan gagal
            console.error(error);
        }
    });
}

function reduceAmount(productId) {
    // Kirim permintaan AJAX ke endpoint yang sesuai untuk mengurangi jumlah stok
    // Anda dapat menggunakan library seperti jQuery atau fetch API untuk melakukan permintaan AJAX
    // Contoh menggunakan jQuery:
    $.ajax({
        url: '/reduce_amount/' + productId + '/',
        type: 'POST',
        success: function(response) {
            // Jika permintaan berhasil, perbarui tampilan jumlah stok
            // Misalnya, dengan mengubah teks pada elemen HTML yang sesuai
            $('#amount-' + productId).text(response.amount);
        },
        error: function(xhr, status, error) {
            // Tangani kesalahan jika permintaan gagal
            console.error(error);
        }
    });
}